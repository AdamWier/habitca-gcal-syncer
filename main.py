import typer
from dotenv import load_dotenv

from google_handler.get_google import get_google
from habitica_handler.get_habitica import get_habitica

load_dotenv()


def main():
    eventsToSync = get_google()

    habiticaTasks = get_habitica()

    eventsToUpdateDailies = filter(
        lambda event: habiticaTasks.get("dailies").get(event.get("text")),
        eventsToSync.get("events"),
    )
    eventsToCreateDailies = filter(
        lambda event: not habiticaTasks.get("dailies").get(event.get("text")),
        eventsToSync.get("events"),
    )

    print(list(eventsToUpdateDailies))
    print(list(eventsToCreateDailies))


if __name__ == "__main__":
    typer.run(main)
