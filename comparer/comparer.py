from .confirm_sync_operations import confirm_sync_operations


def comparer(googleEvents, habiticaTasks):
    eventsToUpdateDailies = list(
        filter(
            lambda event: habiticaTasks.get("dailies").get(event.get("text")),
            googleEvents.get("events"),
        )
    )
    eventsToCreateDailies = list(
        filter(
            lambda event: not habiticaTasks.get("dailies").get(event.get("text")),
            googleEvents.get("events"),
        )
    )

    userAnswers = confirm_sync_operations(eventsToUpdateDailies, eventsToCreateDailies)

    print(userAnswers)
