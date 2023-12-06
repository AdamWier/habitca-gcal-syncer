from datetime import datetime
from functools import reduce

from emoji import replace_emoji


def create_event_day_dictionary(events):
    return reduce(event_organizer, events, {})


def event_organizer(dictionary, event):
    key = replace_emoji(event.get("summary"), replace="").strip()
    daysToAdd = dictionary.get(key, [])[:]
    dayString = event.get("start").get("dateTime")
    weekdayIndex = datetime.strptime(dayString, "%Y-%m-%dT%H:%M:%S%z").weekday()
    weekdays = ["m", "t", "w", "th", "f", "s", "su"]
    daysToAdd.append(weekdays[weekdayIndex])
    updatedDaysToAdd = list(set(daysToAdd))
    dictionary[key] = updatedDaysToAdd
    return dictionary
