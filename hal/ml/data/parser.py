#!/usr/bin/env python
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


""" Parsers for raw databases """

import csv


class Parser(object):
    """ Mother of all data-files parsers """

    def __init__(self, database_file):
        """ :param database_file: a raw .csv file that contains any data
        about anything """

        object.__init__(self)
        self.database_file = database_file
        self.lines = self.get_lines()  # list of lines in database

    def get_lines(self):
        """
        :return: [] of str
            Lines in file
        """

        with open(self.database_file) as data:
            self.lines = data.readlines()  # store data in arrays
        return self.lines


class CSVParser(Parser):
    """ Parses CSV data files """

    def __init__(self, database_file):
        """ :param database_file: a raw .csv file that contains any data
        about anything """

        Parser.__init__(self, database_file)
        self.data = []

    def parse_data(self):
        """ store values in array, store lines in array; the result is a 2D
        matrix """

        with open(self.database_file) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=",", quotechar="\"")
            for row in csv_reader:
                self.data.append(row)

        return self.data


def parse_csv_file(file_path):
    """
    :param file_path: str
        Path to file to parse
    :return: tuple [], [] of []
        headers of csv file and data
    """

    raw_data = CSVParser(file_path).parse_data()
    return raw_data[0], raw_data[1:]  # headers, data


def get_list_of_dict_from_csv(file_path):
    """
    :param file_path: str
        Path to file to parse
    :return: (generator of) [] of {}
        List of dicts with data from .csv file
    """

    reader = csv.DictReader(open(file_path, "r"))
    for row in reader:
        if row:
            yield row
