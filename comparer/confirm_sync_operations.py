from InquirerPy import prompt
from InquirerPy.base.control import Choice


def confirm_sync_operations(eventsToUpdateDailies, eventsToCreateDailies):
    questions = [
        {
            "type": "checkbox",
            "message": "Confirm the dailies to be updated",
            "name": "dailiesToUpdate",
            "choices": list(
                map(
                    lambda event: Choice(event, event.get("text"), enabled=True),
                    eventsToUpdateDailies,
                )
            ),
        },
        {
            "type": "checkbox",
            "message": "Confirm dailies to be created",
            "name": "dailiesToCreate",
            "choices": list(
                map(
                    lambda event: Choice(event, event.get("text"), enabled=False),
                    eventsToCreateDailies,
                )
            ),
        },
        {
            "type": "confirm",
            "message": "Confirm the sync",
            "name": "confirmation",
            "default": False,
        },
    ]

    return prompt(questions)
