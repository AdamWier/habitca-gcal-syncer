from functools import reduce


def create_day_by_daily_dictionary(dailies):
    return reduce(daily_organizer, dailies, {})


def daily_organizer(dictionary, daily):
    key = daily.get("text")
    daysToAdd = dictionary.get(key, [])[:]
    days = list(
        filter(lambda day: daily.get("repeat").get(day), daily.get("repeat").keys())
    )
    daysToAdd.extend(days)
    updatedDaysToAdd = list(set(daysToAdd))
    dictionary[key] = updatedDaysToAdd
    return dictionary
