from functools import partial

from .confirm_sync_operations import confirm_sync_operations
from .prepare_request_information import prepare_request_information


def request_preparer(google_events, habitica_tasks):
    events_to_update_dailies = list(
        filter(
            lambda event: habitica_tasks.get("dailies").get(event.get("text")),
            google_events.get("recurring_events"),
        )
    )
    events_to_create_dailies = list(
        filter(
            lambda event: not habitica_tasks.get("dailies").get(event.get("text")),
            google_events.get("recurring_events"),
        )
    )

    todos_to_create = list(
        filter(
            lambda event: not any(
                todo.get("text", "") in event.get("text")
                for todo in habitica_tasks.get("todos")
            ),
            google_events.get("non_recurring_events"),
        )
    )

    user_answers = confirm_sync_operations(
        events_to_update_dailies, events_to_create_dailies, todos_to_create
    )

    create_todo_requests = list(
        map(
            lambda answer: {
                "url": "https://habitica.com/api/v3/tasks/user",
                "params": {
                    "type": "todo",
                    "text": answer.get("text"),
                },
                "verb": "post",
            },
            user_answers.get("todosToCreate"),
        )
    )

    prepare_request_information_with_habitica_dailies = partial(
        prepare_request_information, habitica_tasks=habitica_tasks.get("dailies")
    )

    update_daily_request_information = list(
        map(
            prepare_request_information_with_habitica_dailies,
            user_answers.get("dailiesToUpdate"),
        )
    )

    update_daily_requests = list(
        map(
            lambda information: {
                "url": f"https://habitica.com/api/v3/tasks/{information.get('id')}",
                "params": {"repeat": information.get("repeat")},
                "verb": "put",
            },
            update_daily_request_information,
        )
    )

    create_daily_request_information = list(
        map(
            prepare_request_information_with_habitica_dailies,
            user_answers.get("dailiesToCreate"),
        )
    )

    create_daily_requests = list(
        map(
            lambda information: {
                "url": "https://habitica.com/api/v3/tasks/user",
                "params": {
                    "repeat": information.get("repeat"),
                    "type": "daily",
                    "text": information.get("text"),
                },
                "verb": "post",
            },
            create_daily_request_information,
        )
    )

    return {
        "update_daily_requests": update_daily_requests,
        "create_daily_requests": create_daily_requests,
        "create_todo_requests": create_todo_requests,
    }
