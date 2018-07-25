#!/usr/bin/env python
# coding: utf-8

# Copyright 2016-2018 Stefano Fogarollo
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

""" Various tools and utilities to deal with database and machine learning. """

import numpy as np


def pearson(lst1, lst2):
    """ Pearson coefficient of arrays"""

    return np.corrcoef(lst1, lst2)[0][1]


def normalize_array(arr):
    """
    :param arr: [] of float
        Array of floats
    :return: [] of float
        Normalized (in [0, 1]) input array
    """

    np_arr = np.array(arr)
    x_normalized = np_arr / np_arr.max(axis=0)
    return list(x_normalized)
