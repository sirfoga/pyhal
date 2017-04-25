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


import time


def get_time_eta(total_done, total, start_time):
    """
    :param total_done: int
        Item processed
    :param total: int
        Total number of items to process
    :param start_time: time (s since epoch)
        Time of start processing items
    :return: {} <str, int>
        Each key is the time unit, each value is eta time
    """

    time_done = int(time.time()) - start_time  # time spent processing items
    speed = total_done / time_done  # avg speed processing items
    total_to_go = total - total_done  # items to go
    seconds_to_go = int(total_to_go / speed)  # eta time
    minutes_to_go = int(seconds_to_go / 60.0)
    hours_to_go = int(minutes_to_go / 60.0)
    days_to_go = int(hours_to_go / 24.0)

    return {
        "s": seconds_to_go,
        "m": minutes_to_go,
        "h": hours_to_go,
        "d": days_to_go
    }
