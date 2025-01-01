from InquirerPy import prompt
from InquirerPy.base.control import Choice


def confirm_sync_operations(
    eventsToUpdateDailies,
    eventsToCreateDailies,
    todos_to_create,
    dailies_not_found_as_pseudo_event,
):
    def give_array(x):
        return []

    def get_choices_from_events(events, default_enabled):
        return list(
                map(
                    lambda event: Choice(event, event.get("text"), enabled=default_enabled),
                    events,
                )
            )
    
    update_choices = get_choices_from_events(eventsToUpdateDailies, True)

    dailies_to_remove_choices = get_choices_from_events(dailies_not_found_as_pseudo_event, False)
    
    dailies_to_create_choices = get_choices_from_events(eventsToCreateDailies, False)

    todos_to_create_choices = get_choices_from_events(todos_to_create, False)

    update_question = {
            "type": "checkbox",
            "message": "Confirm the dailies to be updated",
            "name": "dailiesToUpdate",
            "choices": update_choices,
        } if len(update_choices) else {
            "type": "confirm",
            "message": "No dailies to update",
            "default": True,
            "name": "dailiesToUpdate",
            "filter": give_array,
        }
    
    remove_question = {
            "type": "checkbox",
            "message": "Confirm the dailies that will be removed this week",
            "name": "dailiesToRemove",
            "choices": dailies_to_remove_choices,
        } if len(dailies_to_remove_choices) else {
            "type": "confirm",
            "message": "No dailies to remove",
            "default": True,
            "name": "dailiesToRemove",
            "filter": give_array,
        }

    create_question = {
            "type": "checkbox",
            "message": "Confirm dailies to be created",
            "name": "dailiesToCreate",
            "choices": list(
                map(
                    lambda event: Choice(event, event.get("text"), enabled=False),
                    eventsToCreateDailies,
                )
            ),
        } if len(eventsToCreateDailies) else {
            "type": "confirm",
            "message": "No dailies to create",
            "default": True,
            "name": "dailiesToCreate",
            "filter": give_array,
        }

    todo_create_question = {
        "type": "checkbox",
            "message": "Confirm todos to be created",
            "name": "todosToCreate",
            "choices": todos_to_create_choices,
        } if len(todos_to_create_choices) else {
            "type": "confirm",
            "message": "No to dos to create",
            "default": True,
            "name": "todosToCreate",
            "filter": give_array,
        }
    
    
    questions = [
        update_question,
        remove_question,
        create_question,
        todo_create_question,
        {
            "type": "confirm",
            "message": "Confirm the sync",
            "name": "confirmation",
            "default": False,
        },
    ]

    return prompt(questions)
