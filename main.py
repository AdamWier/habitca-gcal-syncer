import typer
from dotenv import load_dotenv

from get_information import get_information
from request_preparer.request_preparer import request_preparer
from utils.send_multiple_requests import send_multiple_requests

load_dotenv()


def main():
    information = get_information()

    request_information = request_preparer(
        information["google_events"], information["habitica_tasks"]
    )

    responses = send_multiple_requests(request_information.get("update_requests"))

    print(responses)


if __name__ == "__main__":
    typer.run(main)
