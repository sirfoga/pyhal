# -*- coding: utf-8 -*-

"""Parse, convert times formats """

from datetime import datetime

MONTHS_NAMES = [
    datetime.strftime(datetime(year=1, month=m, day=1), "%B")
    for m in range(1, 13)
]  # names of each month
MONTHS = {
    i + 1: MONTHS_NAMES[i] for i in range(len(MONTHS_NAMES))
}  # dict <month index: month name>


def parse_hh_mm_ss(string):
    """Parses raw time

    :param string: Hours minutes and seconds in the form hh
    :returns: Time parsed

    """
    string = str(string).strip()  # discard gibberish
    split_count = string.count(":")
    if split_count == 2:  # hh:mm:ss
        return datetime.strptime(str(string).strip(), "%H:%M:%S").time()
    elif split_count == 1:  # mm:ss
        return datetime.strptime(str(string).strip(), "%M:%S").time()

    return datetime.strptime(str(string).strip(), "%S").time()


def get_seconds(string):
    """Gets seconds from raw time

    :param string: Datetime
    :returns: Seconds in time

    """
    parsed_string = parse_hh_mm_ss(string)  # get times
    total_seconds = parsed_string.second
    total_seconds += parsed_string.minute * 60.0
    total_seconds += parsed_string.hour * 60.0 * 60.0
    return total_seconds


def parse_hh_mm(string):
    """Parses raw time

    :param string: Hours and minutes
    :returns: Time parsed

    """
    string = str(string).strip()  # discard gibberish
    split_count = string.count(":")
    if split_count == 1:  # hh:mm
        return datetime.strptime(str(string).strip(), "%H:%M").time()

    return datetime.strptime(str(string).strip(), "%M").time()
