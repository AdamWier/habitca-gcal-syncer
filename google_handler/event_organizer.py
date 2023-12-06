from datetime import datetime
from functools import reduce

from emoji import replace_emoji


def create_text_day_pairs(events):
    eventDayDictionary = reduce(event_organizer, events, {})
    textDayPairs = list(
        map(
            lambda key: {"days": eventDayDictionary[key], "text": key},
            eventDayDictionary.keys(),
        )
    )
    return textDayPairs


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
