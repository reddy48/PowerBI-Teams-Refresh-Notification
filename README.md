Automating Power BI dataset refresh status notifications to Microsoft Teams using Fabric Notebooks (Python).
## Setup Instructions

1. **Create a Teams Incoming Webhook**
   - Add the connector in your Teams channel and copy the Webhook URL.
<img width="754" height="750" alt="image" src="https://github.com/user-attachments/assets/022594c7-7eb0-4451-98de-b9bb2a4f402b" />
<img width="996" height="897" alt="image" src="https://github.com/user-attachments/assets/92b40883-ba44-4af9-8dbb-28b09f0bd091" />

2. **Register a Service Principal in Azure AD**
   - Get `CLIENT_ID`, `CLIENT_SECRET`, and `TENANT_ID`.
<img width="2000" height="431" alt="image" src="https://github.com/user-attachments/assets/bcef0b82-38cb-47de-bdfa-f880f4aabf21" />
<img width="2022" height="257" alt="image" src="https://github.com/user-attachments/assets/173f40c5-5699-4cb7-a15a-5d578f08d519" />

3. **Assign Power BI Permissions**
   - Grant `Dataset.Read.All` under API permissions and enable service principal access in the Power BI admin portal.

4. **Configure the Notebook**
   - Clone this repo, open `powerbi_refresh_notification.py`.
   - Replace placeholders with your actual values.

5. **Run & Schedule**
   - Run manually to test.
   - Then schedule it in Fabric’s Notebook Scheduler (every 20 mins).

<img width="1144" height="352" alt="Refresh" src="https://github.com/user-attachments/assets/6d1c18a1-ffd3-4260-b4eb-12c38c3a25e4" />

