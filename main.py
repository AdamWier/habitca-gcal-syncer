import typer
from dotenv import load_dotenv

from comparer.comparer import comparer
from google_handler.get_google import get_google
from habitica_handler.get_habitica import get_habitica

load_dotenv()


def main():
    googleEvents = get_google()

    habiticaTasks = get_habitica()

    comparer(googleEvents, habiticaTasks)


if __name__ == "__main__":
    typer.run(main)
