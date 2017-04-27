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


import csv


def save_dicts_to_csv(dicts, output_file):
    """
    :param dicts: [] of {}
        Dictionaries with same values
    :param output_file: str
        Path to output file to write data
    :return: void
        Saves .csv file with posts data
    """

    csv_headers = dicts[0].keys()
    with open(output_file, "w") as o:  # write to file
        dict_writer = csv.DictWriter(o, csv_headers, delimiter=",", quotechar="\"")
        dict_writer.writeheader()
        dict_writer.writerows(dicts)


def save_matrix_to_csv(headers, data, output_file):
    """
    :param headers: [] of str
        Column names
    :param data: matrix ([] of [])
        Data
    :param output_file: str
        Path to output file to write data
    :return: void
        Saves .csv file with data
    """

    with open(output_file, "w") as o:  # write to file
        data_writer = csv.writer(o, delimiter=",")
        data_writer.writerow(headers)  # write headers
        data_writer.writerows(data)  # write all data
