# PowerBI-Teams-Refresh-Notification
Automating Power BI dataset refresh status notifications to Microsoft Teams using Fabric Notebooks (Python).

# Power BI Refresh Notification to Microsoft Teams 🚀

This project demonstrates how to automatically send **Power BI dataset refresh status** 
to Microsoft Teams using **Fabric Python Notebooks**.

## Features
- Fetch Power BI dataset refresh history using REST API
- Filter refreshes from the last 20 minutes
- Send status (✅ Succeeded / ❌ Failed) to Teams via Incoming Webhook
- Scheduled execution in Microsoft Fabric

## Setup
1. Create Teams Incoming Webhook
2. Register Service Principal in Azure AD
3. Configure Fabric Notebook with Workspace & Dataset IDs
4. Schedule notebook every 20 minutes

## Example Output
![Teams Message Screenshot](screenshot.png)

