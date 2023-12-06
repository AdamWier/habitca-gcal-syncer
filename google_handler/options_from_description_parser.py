from functools import reduce
from re import search


def get_options_from_description(description):
    habiticaOptions = search(
        r"\*\*\*HABITICA\*\*\*\n(.+)\n\*\*\*ENDHABITICA\*\*\*", description
    )
    keyValueString = habiticaOptions.group(1) if habiticaOptions else ""
    keyValuePairs = list(
        map(lambda keyValue: keyValue.split(":"), keyValueString.splitlines())
    )
    return reduce(create_options_dictionary, keyValuePairs, {})


def create_options_dictionary(dictionary, keyValuePair):
    dictionary[keyValuePair[0].strip()] = keyValuePair[1].strip()
    return dictionary
