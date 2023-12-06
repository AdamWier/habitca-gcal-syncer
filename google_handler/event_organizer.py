from datetime import datetime
from functools import reduce

from emoji import replace_emoji

from .options_from_description_parser import get_options_from_description


def create_text_day_pairs(events):
    eventDayDictionary = reduce(event_organizer, events, {})
    textDayPairs = list(
        map(
            lambda key: {"days": eventDayDictionary[key], "text": key},
            eventDayDictionary.keys(),
        )
    )
    return textDayPairs


def get_habitica_name(event):
    description = event.get("description", None)
    summary = replace_emoji(event.get("summary"), replace="").strip()
    if description is None:
        return summary
    optionsDictionary = get_options_from_description(description)
    return optionsDictionary.get("sync_name", summary)


def event_organizer(dictionary, event):
    key = get_habitica_name(event)
    daysToAdd = dictionary.get(key, [])[:]
    dayString = event.get("start").get("dateTime")
    weekdayIndex = datetime.strptime(dayString, "%Y-%m-%dT%H:%M:%S%z").weekday()
    weekdays = ["m", "t", "w", "th", "f", "s", "su"]
    daysToAdd.append(weekdays[weekdayIndex])
    updatedDaysToAdd = list(set(daysToAdd))
    dictionary[key] = updatedDaysToAdd
    return dictionary
