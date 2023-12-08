import typer
from dotenv import load_dotenv

from get_information import get_information
from request_preparer.request_preparer import request_preparer

load_dotenv()


def main():
    information = get_information()

    request_preparer(information["googleEvents"], information["habiticaTasks"])


if __name__ == "__main__":
    typer.run(main)
