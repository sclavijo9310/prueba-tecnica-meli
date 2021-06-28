import localization as lx
from collections import OrderedDict
from core.exceptions import InvalidDistances, MissingData
from core.data import satellites_data


def get_location(distances):
    if len(distances) != 3:
        raise InvalidDistances('Invalid distances values count (must be 3)')
    else:
        # https://github.com/kamalshadi/Localization
        p = lx.Project(mode='2D', solver='LSE')

        for satellite in satellites_data:
            p.add_anchor(satellite.name, (satellite.x, satellite.y))

        t, label = p.add_target()
        for satellite, distance in zip(satellites_data, distances):
            t.add_measure(satellite.name, distance)

        p.solve()

        return t.loc.x, t.loc.y


def _count_total_words(messages):
    result = []
    for arr_messages in messages:
        result = result + [message for message in arr_messages if len(message) > 0]  # Filter out spaces

    return len(OrderedDict.fromkeys(result))  # ToDo: Contemplate repeated words...


# Returns all list messages with same length (max total possible words count)
def _get_normalized_messages(messages, total_words):
    result = []
    for arr_messages in messages:
        while len(arr_messages) < total_words:
            arr_messages.insert(0, '')  # Complete list if is required (ensure equal length to all list)
        result.append(arr_messages[-total_words:])

    return result


def get_message(messages):
    total_words = _count_total_words(messages)
    result = [''] * total_words
    normalized_messages = _get_normalized_messages(messages, total_words)
    for arr_messages in normalized_messages:
        for i in range(total_words):
            # Check current satellite message position for missing word
            if len(result[i]) == 0 and len(arr_messages[i]) > 0:
                result[i] = arr_messages[i]

    return ' '.join(result)


def validate_data():
    for satellite in satellites_data:
        if satellite.distance is None or satellite.message is None or len(satellite.message) == 0:
            raise MissingData()
