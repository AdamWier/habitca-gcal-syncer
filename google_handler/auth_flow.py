import os

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = ["https://www.googleapis.com/auth/calendar.readonly"]


def google_auth_flow():
    existingCreds = (
        Credentials.from_authorized_user_file("token.json", SCOPES)
        if os.path.exists("token.json")
        else None
    )

    if existingCreds and existingCreds.valid:
        return existingCreds

    if existingCreds and existingCreds.expired and existingCreds.refresh_token:
        existingCreds.refresh(Request())
        return existingCreds
    else:
        flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
        newCreds = flow.run_local_server(port=0)

        with open("token.json", "w") as token:
            token.write(newCreds.to_json())

        return newCreds
