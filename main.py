import json

import typer
from dotenv import load_dotenv

from google_handler.get_google import get_google
from habitica_handler.get_habitica import get_habitica

load_dotenv()


def main():
    eventsToSync = get_google()

    print(
        json.dumps(
            eventsToSync,
            indent=2,
        )
    )

    habiticaTasks = get_habitica()

    print(
        json.dumps(
            habiticaTasks,
            indent=2,
        )
    )

    print()


if __name__ == "__main__":
    typer.run(main)
