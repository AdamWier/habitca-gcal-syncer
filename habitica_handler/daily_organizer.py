from functools import reduce

def create_day_by_daily_text_dictionary(dailies):
    return reduce(daily_organizer, dailies, {})


def daily_organizer(dictionary, daily):
    key = daily.get("text").strip()

    processedDaily = dictionary.get(key, {"id": "", "days": []})

    existingDays = processedDaily.get("days", [])
    days = list(
        filter(lambda day: daily.get("repeat").get(day), daily.get("repeat").keys())
    )
    existingDays.extend(days)
    updatedDaysToAdd = list(set(existingDays))

    id = daily.get("id")

    dictionary[key] = {"id": id, "days": updatedDaysToAdd}

    return dictionary
