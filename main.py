import typer
from dotenv import load_dotenv

from find_modifications.get_possible_event_modifications import (
    get_possible_event_modifications,
)
from get_information import get_information
from request_preparer.request_preparer import request_preparer
from utils.send_multiple_requests import send_multiple_requests

load_dotenv()


def main():
    information = get_information()

    user_answers = get_possible_event_modifications(
        information["google_events"], information["habitica_tasks"]
    )

    if not user_answers.get("confirmation"):
        return

    request_information = request_preparer(user_answers, information["habitica_tasks"])

    allRequests = sum(request_information.values(), [])
    responses = send_multiple_requests(allRequests)

    print(responses)


if __name__ == "__main__":
    typer.run(main)
