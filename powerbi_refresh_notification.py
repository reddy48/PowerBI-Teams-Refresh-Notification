import requests
from datetime import datetime, timedelta, timezone

# ==== CONFIG ====
TENANT_ID = "<YOUR_TENANT_ID>"
CLIENT_ID = "<YOUR_CLIENT_ID>"
CLIENT_SECRET = "<YOUR_CLIENT_SECRET>"

WORKSPACE_ID = "<YOUR_WORKSPACE_ID>"   # Your workspace ID
DATASET_ID = "<YOUR_DATASET_ID>"       # Your dataset ID
WEBHOOK_URL = "<YOUR_TEAMS_WEBHOOK_URL>"

# ==== GET ACCESS TOKEN ====
def get_access_token(tenant_id, client_id, client_secret):
    url = f"https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token"
    payload = {
        "client_id": client_id,
        "scope": "https://analysis.windows.net/powerbi/api/.default",
        "client_secret": client_secret,
        "grant_type": "client_credentials"
    }
    resp = requests.post(url, data=payload)
    resp.raise_for_status()
    return resp.json()["access_token"]

access_token = get_access_token(TENANT_ID, CLIENT_ID, CLIENT_SECRET)
headers = {"Authorization": f"Bearer {access_token}"}

# ==== GET DATASET NAME ====
datasets_url = f"https://api.powerbi.com/v1.0/myorg/groups/{WORKSPACE_ID}/datasets"
resp_datasets = requests.get(datasets_url, headers=headers)
resp_datasets.raise_for_status()
datasets = resp_datasets.json().get("value", [])

dataset_map = {d["id"]: d["name"] for d in datasets}
dataset_name = dataset_map.get(DATASET_ID, DATASET_ID)

# ==== FETCH REFRESH HISTORY ====
url = f"https://api.powerbi.com/v1.0/myorg/groups/{WORKSPACE_ID}/datasets/{DATASET_ID}/refreshes?$top=10"
response = requests.get(url, headers=headers)
response.raise_for_status()
refreshes = response.json().get("value", [])

# ==== FILTER LAST 20 MINUTES ====
cutoff_time = datetime.now(timezone.utc) - timedelta(minutes=20)
recent_refreshes = []

for r in refreshes:
    start = datetime.fromisoformat(r["startTime"].replace("Z", "+00:00"))
    if start > cutoff_time:
        row = {
            "Dataset": dataset_name,
            "Start": r["startTime"],
            "End": r["endTime"],
            "Status": r["status"]
        }
        recent_refreshes.append(row)

# ==== ONLY SEND IF REFRESH FOUND ====
if recent_refreshes:
    # Build table
    table = "| Dataset | Start | End | Status |\n"
    table += "|---------|-------|-----|--------|\n"
    for r in recent_refreshes:
        status_icon = "🟢" if r["Status"].lower() == "succeeded" else "🔴"
        table += f"| {r['Dataset']} | {r['Start']} | {r['End']} | {status_icon} {r['Status']} |\n"

    payload = {
        "@type": "MessageCard",
        "@context": "http://schema.org/extensions",
        "summary": "Power BI Refresh Report",
        "themeColor": "0078D7",
        "title": "🔄 Power BI Refresh Report (Last 20 minutes)",
        "text": table
    }

    # Send notification
    resp = requests.post(WEBHOOK_URL, json=payload)
    if resp.status_code == 200:
        print("✅ Message sent successfully to Teams")
    else:
        print(f"❌ Failed to send message: {resp.status_code}, {resp.text}")
else:
    print("ℹ️ No refresh activity in last 20 minutes, skipping Teams notification.")
