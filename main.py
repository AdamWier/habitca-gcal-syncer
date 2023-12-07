import typer
from dotenv import load_dotenv

from google_handler.get_google import get_google
from habitica_handler.get_habitica import get_habitica
from request_preparer.request_preparer import request_preparer

load_dotenv()


def main():
    googleEvents = get_google()

    habiticaTasks = get_habitica()

    request_preparer(googleEvents, habiticaTasks)


if __name__ == "__main__":
    typer.run(main)
