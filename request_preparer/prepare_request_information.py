import collections
from functools import reduce


def prepare_request_information(event_daily, habitica_tasks):
    habitica_daily = habitica_tasks.get(event_daily.get("text"))
    if habitica_daily:
        days_are_same = collections.Counter(event_daily.get("days")) == collections.Counter(
            habitica_daily.get("days")
        )
        if days_are_same:
            return None
    days = convert_days_for_request(event_daily.get("days"))
    return {
        "id": habitica_daily.get("id") if habitica_daily else "",
        "repeat": days,
        "text": event_daily.get("text"),
    }


def mark_days_as_true(dictionary, day):
    dictionary[day] = True
    return dictionary


def convert_days_for_request(dayList):
    default_days = {
        "m": False,
        "t": False,
        "w": False,
        "th": False,
        "f": False,
        "s": False,
        "su": False,
    }

    return reduce(mark_days_as_true, dayList, default_days)
