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


""" properties of shell and terminal (cmd) """

import subprocess
import sys
from subprocess import call


def printf(data, max_length):
    """
    :param data: text to display
    :param max_length: max length available
    :return: good representation of text
    """

    if len(data) > max_length + 2:
        return '{:.{}}'.format(data, max_length).ljust(max_length) + '..'
    else:
        return '{:.{}}'.format(data, max_length)


def erase_last_line():
    """
    :return: erases last line in shell
    """

    sys.stdout.write('\033[F')


def size():
    """
    :return: size of shell
    """

    def get_shell_size(shell):
        """
        :param shell: terminal
        :return: size of given shell
        """
        try:
            import fcntl, termios, struct, os
            return struct.unpack('hh', fcntl.ioctl(shell, termios.TIOCGWINSZ, '1234'))
        except:
            return

    size = get_shell_size(0) or get_shell_size(1) or get_shell_size(2)

    if not size:
        size = [24, 80]  # default size

    return size


def get_formatted(data, max_length):
    """
    :param data: text to display
    :param max_length: max length available
    :return: good representation of text
    """

    if len(data) > max_length + 2:
        return '{:.{}}'.format(data, max_length).ljust(max_length) + '..'
    else:
        return '{:.{}}'.format(data, max_length)


def call_command(command):
    """
    :param command: command to call
    :return: calls given command
    """

    shell = command.split(' ')
    call(shell)


def get_command(command):
    """
    :param command: command to call
    :return: get result from given command
    """
    
    shell = command.split(' ')
    return subprocess.check_output(shell)
