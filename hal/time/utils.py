# !/usr/bin/python3
# coding: utf-8

# Copyright 2016-2018 Stefano Fogarollo
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


""" Parse, convert time formats """

from datetime import datetime

MONTHS_NAMES = [datetime.strftime(datetime(year=1, month=m, day=1), "%B") for m
                in range(1, 13)]  # names of each month
MONTHS = {
    i + 1: MONTHS_NAMES[i] for i in range(len(MONTHS_NAMES))
    }  # dict <month index: month name>


def parse_hh_mm_ss(string):
    """
    :param string: str
        Hours, minutes and seconds in the form hh:mm:ss to parse
    :return: datetime.time
        Time parsed
    """

    string = str(string).strip()  # discard gibberish
    split_count = string.count(":")
    if split_count == 2:  # hh:mm:ss
        return datetime.strptime(str(string).strip(), "%H:%M:%S").time()
    elif split_count == 1:  # mm:ss
        return datetime.strptime(str(string).strip(), "%M:%S").time()

    return datetime.strptime(str(string).strip(), "%S").time()


def get_seconds(string):
    """
    :param string: str
        Datetime in the form %H:%M:%S
    :return: int
        Seconds in time
    """

    parsed_string = parse_hh_mm_ss(string)  # get time
    total_seconds = parsed_string.second
    total_seconds += parsed_string.minute * 60.0
    total_seconds += parsed_string.hour * 60.0 * 60.0
    return total_seconds


def parse_hh_mm(string):
    """
    :param string: str
        Hours and minutes in the form hh:mm to parse
    :return: datetime.time
        Time parsed
    """

    string = str(string).strip()  # discard gibberish
    split_count = string.count(":")
    if split_count == 1:  # hh:mm
        return datetime.strptime(str(string).strip(), "%H:%M").time()

    return datetime.strptime(str(string).strip(), "%M").time()
