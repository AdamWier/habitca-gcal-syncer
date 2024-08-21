from .confirm_sync_operations import confirm_sync_operations


def get_possible_event_modifications(google_events, habitica_tasks):
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

    recurring_event_names = list(
        map(lambda event: event.get("text"), google_events.get("recurring_events"))
    )

    dailies_not_found = list(
        filter(
            lambda daily_text: daily_text not in recurring_event_names,
            habitica_tasks.get("dailies").keys(),
        )
    )

    dailies_not_found_as_pseudo_event = list(
        map(lambda daily_text: {"text": daily_text, "days": []}, dailies_not_found)
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
        events_to_update_dailies,
        events_to_create_dailies,
        todos_to_create,
        dailies_not_found_as_pseudo_event,
    )

    return user_answers
