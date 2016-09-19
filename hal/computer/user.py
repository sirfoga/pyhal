# !/usr/bin/python
# coding: utf_8

# Copyright 2016 Stefano Fogarollo
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


""" representation of multi-user os """

import os
import platform
import sys

from hal.regex.strings import Color


def pyversion():
    """
    :return: print python version installed in computer
    """

    return 'Python ' + sys.version + ' on ' + sys.platform


def username():
    """
    :return: username of current user
    """

    return os.environ["USER"]


def get_os():
    """
    :return: current OS
    """

    return platform.platform()


def home_dir():
    """
    :return: path to home directory
    """

    return os.path.expanduser('~')


def work_dir():
    """
    :return: path to working directory
    """

    return os.getcwd()


def answer(question):
    """
    :param question: prompts question [y/n]
    :return: return True iff ans is 'y'
    """

    ans = input(question + ' [y/n]\n')
    if ans[0] == 'n':
        return False
    else:
        return True


def welcome(presentation):
    """
    :param presentation: string to introduce script
    :return: introduce script
    """
    
    introduction = 'Hello ' + Color.BOLD + username() + Color.END + '!'
    introduction += '\nrunning ' + Color.BOLD + pyversion() + Color.END
    introduction += '\nunder' + Color.BOLD + os() + Color.END
    introduction += '\nin ' + Color.BOLD + work_dir() + Color.END
    introduction += '\n' + str(presentation)
    return introduction
