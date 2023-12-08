from google_handler.get_google import get_google
from habitica_handler.get_habitica import get_habitica
from utils.with_spinner import with_spinner


@with_spinner("Getting information...")
def get_information():
    googleEvents = get_google()

    habiticaTasks = get_habitica()

    return {
        "googleEvents": googleEvents,
        "habiticaTasks": habiticaTasks,
    }
