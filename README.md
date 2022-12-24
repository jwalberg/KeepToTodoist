# KeepToTodoist
Copy Google Keep notes to Todoist to manage Google Home making life difficult for Todoist users

## Setup
If you're using two factor authentication with your Google account(as you should), this won't work, so you'll need to set up an App password here: https://myaccount.google.com/apppasswords

You can get a Todoist API key here: https://todoist.com/app/settings/integrations/developer

Put the API key, the login details, and your chosen Todoist project in config.yml. The run KeepToToDoist.py in Python. I've got this running hourly using Windows scheduled tasks.
