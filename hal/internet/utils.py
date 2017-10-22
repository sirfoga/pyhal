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


""" Internet tools """

import socket
import time


def is_internet_on(host="8.8.8.8", port=53, timeout=3):
    """
    :param host: str
        Google-public-dns-a.google.com
    :param port: int
        53/tcp
    :param timeout: int
        Seconds
    :return: bool
        True iff machine has internet connection
    """

    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return True
    except:
        return False


def wait_until_internet(time_between_attempts=3, max_attempts=10):
    """
    :param time_between_attempts: int
        Seconds between 2 consecutive attempts
    :param max_attempts: int
        Max number of attempts to try
    :return: bool
        True iff there is internet connection
    """

    counter = 0
    while not is_internet_on():
        time.sleep(time_between_attempts)  # wait until internet is on
        counter += 1

        if counter > max_attempts:
            return False

    return True
