from functools import partial

from .confirm_sync_operations import confirm_sync_operations
from .prepare_request_information import prepare_request_information


def request_preparer(google_events, habitica_tasks):
    events_to_update_dailies = list(
        filter(
            lambda event: habitica_tasks.get("dailies").get(event.get("text")),
            google_events.get("events"),
        )
    )
    events_to_create_dailies = list(
        filter(
            lambda event: not habitica_tasks.get("dailies").get(event.get("text")),
            google_events.get("events"),
        )
    )

    user_answers = confirm_sync_operations(
        events_to_update_dailies, events_to_create_dailies
    )

    prepare_request_information_with_habitica_tasks = partial(
        prepare_request_information, habitica_tasks=habitica_tasks
    )

    update_request_information = list(
        map(
            prepare_request_information_with_habitica_tasks,
            user_answers.get("dailiesToUpdate"),
        )
    )

    update_requests = list(
        map(
            lambda information: {
                "url": f"https://habitica.com/api/v3/tasks/{information.get('id')}",
                "params": {"repeat": information.get("repeat")},
            },
            update_request_information,
        )
    )

    return {"update_requests": update_requests}
