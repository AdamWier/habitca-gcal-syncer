from functools import partial

from .confirm_sync_operations import confirm_sync_operations
from .prepare_request_information import prepare_request_information


def request_preparer(googleEvents, habiticaTasks):
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

    prepareRequestInformationWithHabiticaTasks = partial(
        prepare_request_information, habiticaTasks=habiticaTasks
    )

    updateRequestInformation = list(
        map(
            prepareRequestInformationWithHabiticaTasks,
            userAnswers.get("dailiesToUpdate"),
        )
    )

    updateRequests = list(
        map(
            lambda information: {
                "url": f"https://habitica.com/api/v3/tasks/{information.get('id')}",
                "params": {"repeat": information.get("repeat")},
            },
            updateRequestInformation,
        )
    )

    return {"updateRequests": updateRequests}
