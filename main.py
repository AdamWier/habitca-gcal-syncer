import json

import typer
from dotenv import load_dotenv

from google_handler.get_google import get_google
from habitica_handler.call_habitica import call_habitica

load_dotenv()


def main():
    eventsToSync = get_google()

    print(
        json.dumps(
            eventsToSync,
            indent=2,
        )
    )

    habiticaTasks = call_habitica()

    print(
        json.dumps(
            habiticaTasks,
            indent=2,
        )
    )


if __name__ == "__main__":
    typer.run(main)
