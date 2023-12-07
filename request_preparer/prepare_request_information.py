from functools import reduce


def prepare_request_information(eventDaily, habiticaTasks):
    habiticaDaily = habiticaTasks.get("dailies").get(eventDaily.get("text"))
    days = convert_days_for_request(eventDaily.get("days"))
    return {
        "id": habiticaDaily.get("id"),
        "repeat": days,
        "text_for_debugging_only": eventDaily.get("text"),
    }


def mark_days_as_true(dictionary, day):
    dictionary[day] = True
    return dictionary


def convert_days_for_request(dayList):
    defaultDays = {
        "m": False,
        "t": False,
        "w": False,
        "th": False,
        "f": False,
        "s": False,
        "su": False,
    }

    return reduce(mark_days_as_true, dayList, defaultDays)
