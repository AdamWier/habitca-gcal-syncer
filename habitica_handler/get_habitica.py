from .call_habitica import call_habitica
from .daily_organizer import create_day_by_daily_text_dictionary


def get_habitica():
    tasks = call_habitica()

    dailies = list(filter(lambda task: task.get("type") == "daily", tasks))
    reduced_dailies = create_day_by_daily_text_dictionary(dailies)

    todos = list(filter(lambda task: task.get("type") == "todo", tasks))

    return {"dailies": reduced_dailies, "todos": todos}
