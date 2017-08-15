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


""" Typical operations on strings made easy """

from difflib import SequenceMatcher


def how_similar_are(str1, str2):
    """
    :param str1: str
        First string
    :param str2: str
        Second string
    :return: float in [0, 1]
        Similarity of a VS b
    """

    return SequenceMatcher(None, str1, str2).ratio()


def get_average_length_of_word(words):
    """
    :param words: [] of str
        Words
    :return: float
        Average length of word on list
    """

    if not words:
        return 0

    return sum(len(word) for word in words) / len(words)
