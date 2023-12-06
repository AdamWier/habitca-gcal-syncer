from .auth_flow import google_auth_flow
from .event_organizer import create_text_day_pairs
from .get_events import get_events


def get_google():
    events = get_events(google_auth_flow())

    repeatingEvents = list(filter(lambda event: event.get("recurringEventId"), events))
    notFullDayEvents = list(
        filter(lambda event: event.get("start", {}).get("dateTime"), repeatingEvents)
    )
    eventDayDictionary = create_text_day_pairs(notFullDayEvents)

    return {"events": eventDayDictionary}
