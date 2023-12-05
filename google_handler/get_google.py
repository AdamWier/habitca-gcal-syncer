from .auth_flow import google_auth_flow
from .get_events import get_events


def get_google():
    return get_events(google_auth_flow())
