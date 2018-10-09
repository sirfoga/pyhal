# -*- coding: utf-8 -*-

""" Save various data to file """

import csv
import json


class FileSaver:
    """Saves to file"""

    def __init__(self, output_file):
        """
        Arguments:
            output_file: Path to output file to write data
        """
        self.path = output_file

    def write_dicts_to_csv(self, dicts):
        """Saves .csv file with posts data
        :param dicts: Dictionaries with same values
        :param output_file: Path to output file to write data
        :returns: Saves .csv file with posts data
        """
        csv_headers = sorted(dicts[0].keys())
        with open(self.path, "w") as out_file:  # write to file
            dict_writer = csv.DictWriter(
                out_file, csv_headers, delimiter=",", quotechar="\""
            )
            dict_writer.writeheader()
            dict_writer.writerows(dicts)

    def write_matrix_to_csv(self, headers, data):
        """
        :param headers: of str
        :param Column: names
        :param data: matrix
        :param Data: 
        :param output_file: str
        :param Path: to output file to write data
        :returns: void
          Saves .csv file with data
        """
        with open(self.path, "w") as out_file:  # write to file
            data_writer = csv.writer(out_file, delimiter=",")
            data_writer.writerow(headers)  # write headers
            data_writer.writerows(data)  # write all data

    def write_dicts_to_json(self, data):
        """
        :param data: list of
        :param Data: to write
        :param output_file: str
        :param Path: to output file
        :returns: void
          Saves output file as .json
        """
        with open(self.path, "w") as out:
            json.dump(
                data,  # data
                out,  # file handler
                indent=4, sort_keys=True  # pretty print
            )
