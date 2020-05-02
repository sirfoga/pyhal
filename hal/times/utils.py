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


class Timing:
    """Time"""

    def __init__(self, raw):
        """
        :param raw: raw time
        """
        self.raw = str(raw).strip()  # discard gibberish

    def parse_hh_mm_ss(self):
        """Parses raw time

        :return: Time parsed
        """
        split_count = self.raw.count(":")

        if split_count == 2:  # hh:mm:ss
            return datetime.strptime(str(self.raw).strip(), "%H:%M:%S").time()
        elif split_count == 1:  # mm:ss
            return datetime.strptime(str(self.raw).strip(), "%M:%S").time()

        return datetime.strptime(str(self.raw).strip(), "%S").time()

    def get_seconds(self):
        """Gets seconds from raw time

        :return: Seconds in time
        """
        parsed = self.parse_hh_mm_ss()  # get times
        total_seconds = parsed.second
        total_seconds += parsed.minute * 60.0
        total_seconds += parsed.hour * 60.0 * 60.0
        return total_seconds

    def parse_hh_mm(self):
        """Parses raw time

        :return: Time parsed
        """
        split_count = self.raw.count(":")
        if split_count == 1:  # hh:mm
            return datetime.strptime(self.raw, "%H:%M").time()

        return datetime.strptime(self.raw, "%M").time()
