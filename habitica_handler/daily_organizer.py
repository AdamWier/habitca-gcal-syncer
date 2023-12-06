from functools import reduce

from emoji import replace_emoji


def create_day_by_daily_dictionary(dailies):
    return reduce(daily_organizer, dailies, {})


def daily_organizer(dictionary, daily):
    key = daily.get("id")
    processedDaily = dictionary.get(key, {"id": "", "days": [], "text": ""})

    textWithoutEmoji = replace_emoji(daily.get("text"), replace="").strip()

    existingDays = processedDaily.get("days", [])
    days = list(
        filter(lambda day: daily.get("repeat").get(day), daily.get("repeat").keys())
    )
    existingDays.extend(days)
    updatedDaysToAdd = list(set(existingDays))

    dictionary[key] = {"text": textWithoutEmoji, "days": updatedDaysToAdd}

    return dictionary
