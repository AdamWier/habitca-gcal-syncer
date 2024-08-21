from functools import partial

from utils.remove_none_from_list import remove_none_from_list

from .prepare_request_information import prepare_request_information


def request_preparer(user_answers, habitica_tasks):
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

    remove_daily_request_information = remove_none_from_list(
        list(
            map(
                prepare_request_information_with_habitica_dailies,
                user_answers.get("dailiesToRemove"),
            )
        )
    )

    remove_daily_requests = list(
        map(
            lambda information: {
                "url": f"https://habitica.com/api/v3/tasks/{information.get('id')}",
                "params": {"repeat": information.get("repeat")},
                "verb": "put",
            },
            remove_daily_request_information,
        )
    )

    update_daily_request_information = remove_none_from_list(
        list(
            map(
                prepare_request_information_with_habitica_dailies,
                user_answers.get("dailiesToUpdate"),
            )
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
        "remove_daily_requests": remove_daily_requests,
    }
