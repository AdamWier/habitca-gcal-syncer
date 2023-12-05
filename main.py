import json
import os

import requests
import typer
from dotenv import load_dotenv

from google.authFlow import google_auth_flow
from google.getEvents import get_events

load_dotenv()


def main():
    creds = google_auth_flow()
    get_events(creds)

    HABITICA_USER_ID = os.getenv("HABITICA_USER_ID")
    HABITICA_API_KEY = os.getenv("HABITICA_API_KEY")
    print(
        json.dumps(
            json.loads(
                requests.get(
                    "https://habitica.com/api/v3/tasks/user",
                    headers={
                        "x-api-user": HABITICA_USER_ID,
                        "x-api-key": HABITICA_API_KEY,
                    },
                ).content
            ),
            indent=2,
        )
    )


if __name__ == "__main__":
    typer.run(main)
