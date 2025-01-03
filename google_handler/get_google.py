from .auth_flow import google_auth_flow
from .event_organizer import create_text_day_pairs
from .get_events import get_events


def get_google():
    events = get_events(google_auth_flow())

    repeating_events = list(filter(lambda event: event.get("recurringEventId"), events))
    not_full_day_events = list(
        filter(lambda event: event.get("start", {}).get("dateTime"), repeating_events)
    )
    event_day_dictionary = create_text_day_pairs(not_full_day_events)

    non_recurring_events = list(
        filter(lambda event: not event.get("recurringEventId"), events)
    )

    formatted_nonrecurring_events = list(
        map(
            lambda event: {
                "text": event.get("summary").strip()
            },
            non_recurring_events,
        )
    )

    return {
        "recurring_events": event_day_dictionary,
        "non_recurring_events": formatted_nonrecurring_events,
    }
