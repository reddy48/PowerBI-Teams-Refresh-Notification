# PowerBI-Teams-Refresh-Notification
Automating Power BI dataset refresh status notifications to Microsoft Teams using Fabric Notebooks (Python).
## Setup Instructions

1. **Create a Teams Incoming Webhook**
   - Add the connector in your Teams channel and copy the Webhook URL.

2. **Register a Service Principal in Azure AD**
   - Get `CLIENT_ID`, `CLIENT_SECRET`, and `TENANT_ID`.

3. **Assign Power BI Permissions**
   - Grant `Dataset.Read.All` under API permissions and enable service principal access in the Power BI admin portal.

4. **Configure the Notebook**
   - Clone this repo, open `powerbi_refresh_notification.py`.
   - Replace placeholders with your actual values.

5. **Run & Schedule**
   - Run manually to test.
   - Then schedule it in Fabric’s Notebook Scheduler (every 20 mins).


