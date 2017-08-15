# !/usr/bin/python3
# coding: utf-8

# Copyright 2017 Stefano Fogarollo
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from datetime import datetime

MONTHS_NAMES = [datetime.strftime(datetime(year=1, month=m, day=1), "%B") for m
                in range(1, 13)]  # names of each month
MONTHS = {
    i + 1: MONTHS_NAMES[i] for i in range(len(MONTHS_NAMES))
    }  # dict <month index: month name>


def parse_hh_mm_ss(h):
    """
    :param h: str
        Hours, minutes and seconds in the form hh:mm:ss to parse
    :return: datetime.time
        Time parsed
    """

    h = str(h).strip()  # discard jibberish
    split_count = h.count(":")
    if split_count == 2:  # hh:mm:ss
        return datetime.strptime(str(h).strip(), "%H:%M:%S").time()
    elif split_count == 1:  # mm:ss
        return datetime.strptime(str(h).strip(), "%M:%S").time()
    else:  # ss
        return datetime.strptime(str(h).strip(), "%S").time()


def get_seconds(s):
    """
    :param s: str
        Datetime in the form %H:%M:%S
    :return: int
        Seconds in time
    """

    t = parse_hh_mm_ss(s)  # get time
    total_seconds = t.second
    total_seconds += t.minute * 60.0
    total_seconds += t.hour * 60.0 * 60.0
    return total_seconds


def parse_hh_mm(h):
    """
    :param h: str
        Hours and minutes in the form hh:mm to parse
    :return: datetime.time
        Time parsed
    """

    h = str(h).strip()  # discard jibberish
    split_count = h.count(":")
    if split_count == 1:  # hh:mm
        return datetime.strptime(str(h).strip(), "%H:%M").time()
    else:  # mm
        return datetime.strptime(str(h).strip(), "%M").time()