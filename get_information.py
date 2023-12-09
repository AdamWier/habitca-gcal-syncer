from google_handler.get_google import get_google
from habitica_handler.get_habitica import get_habitica
from utils.with_spinner import with_spinner


@with_spinner("Getting information...")
def get_information():
    google_events = get_google()

    habitica_tasks = get_habitica()

    return {
        "google_events": google_events,
        "habitica_tasks": habitica_tasks,
    }
