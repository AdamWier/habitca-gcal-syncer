import json
import os

import requests


def call_habitica():
    HABITICA_USER_ID = os.getenv("HABITICA_USER_ID")
    HABITICA_API_KEY = os.getenv("HABITICA_API_KEY")

    tasks = json.loads(
        requests.get(
            "https://habitica.com/api/v3/tasks/user",
            headers={
                "x-api-user": HABITICA_USER_ID,
                "x-api-key": HABITICA_API_KEY,
            },
        ).content
    ).get("data")

    dailies = list(filter(lambda task: task.get("type") == "daily", tasks))
    todos = list(filter(lambda task: task.get("type") == "todo", tasks))

    return {"dailies": dailies, "todos": todos}
