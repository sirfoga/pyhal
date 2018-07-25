#!/usr/bin/env python
# coding: utf-8


""" Parsers for raw databases """

import csv
import json


class Parser(object):
    """ Mother of all data-files parsers """

    def __init__(self, file_path):
        """
        :param file_path: a raw .csv file that contains any data
            about anything
        """

        object.__init__(self)
        self.path = file_path
        self.lines = None  # list of lines in database

    def get_lines(self):
        """
        :return: [] of str
            Lines in file
        """

        with open(self.path) as data:
            self.lines = data.readlines()  # store data in arrays

        return self.lines


class CSVParser(Parser):
    """ Parses CSV data files """

    def __init__(self, file_path, encoding="utf-8"):
        """
        :param file_path: a raw .csv file that contains any data
            about anything
        :param encoding: str
            Encoding to open file with
        """

        Parser.__init__(self, file_path)
        self.encoding = str(encoding).strip()

    def get_matrix(self):
        """
        :return: store values in array, store lines in array. The result is
            a 2D matrix
        """

        data = []
        with open(self.path, encoding=self.encoding) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=",", quotechar="\"")
            for row in csv_reader:
                data.append(row)

        return data

    def get_headers_data(self):
        """
        :return: tuple [], [] of []
            headers of csv file and data
        """

        data = self.get_matrix()
        return data[0], data[1:]  # headers, data

    def get_dicts(self):
        """
        :return: (generator of) [] of {}
            List of dicts with data from .csv file
        """

        reader = csv.DictReader(open(self.path, "r", encoding=self.encoding))
        for row in reader:
            if row:
                yield row


class JSONParser(Parser):
    def get_content(self):
        with open(self.path, "r") as in_file:
            return json.loads(
                in_file.read()
            )  # read and return json object
