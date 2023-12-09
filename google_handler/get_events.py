import copy
import datetime

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


def get_events(creds):
    try:
        service = build("calendar", "v3", credentials=creds)

        today = datetime.datetime.utcnow().replace(
            hour=0, minute=0, second=0, microsecond=0
        )
        one_week_from_today = copy.copy(today) + datetime.timedelta(days=7)

        events_result = (
            service.events()
            .list(
                calendarId="primary",
                timeMin=today.isoformat() + "Z",
                timeMax=one_week_from_today.isoformat() + "Z",
                singleEvents=True,
                orderBy="startTime",
            )
            .execute()
        )
        events = events_result.get("items", [])

        if not events:
            print("No events found.")
            return

        return events

    except HttpError as error:
        print(f"An error occurred: {error}")
