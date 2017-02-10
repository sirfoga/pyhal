#!/usr/bin/env python
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


""" Parsers for raw databases. """


class Parser(object):
    def __init__(self, database_file):
        """ :param database_file: a raw .csv file that contains any data about anything """

        object.__init__(self)
        self.database_file = database_file
        self.lines = self.get_lines()  # list of lines in database

    def get_lines(self):
        with open(self.database_file) as data:
            self.lines = data.readlines()  # store data in arrays
        return self.lines


class CSVParser(Parser):
    def __init__(self, database_file):
        """ :param database_file: a raw .csv file that contains any data about anything """

        Parser.__init__(self, database_file)
        self.data = []

    def parse_data(self):
        """ store values in array, store lines in array; the result is a 2D matrix"""

        for line in self.lines:
            tokens = line.split(",")
            self.data.append(tokens)

        return self.data
