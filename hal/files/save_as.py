# !/usr/bin/python3
# coding: utf-8


""" Save various data to file """

import csv
import json


def write_dicts_to_csv(dicts, output_file):
    """
    :param dicts: [] of {}
        Dictionaries with same values
    :param output_file: str
        Path to output file to write data
    :return: void
        Saves .csv file with posts data
    """

    csv_headers = sorted(dicts[0].keys())
    with open(output_file, "w") as out_file:  # write to file
        dict_writer = csv.DictWriter(
            out_file, csv_headers, delimiter=",", quotechar="\""
        )
        dict_writer.writeheader()
        dict_writer.writerows(dicts)


def write_matrix_to_csv(headers, data, output_file):
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

    with open(output_file, "w") as out_file:  # write to file
        data_writer = csv.writer(out_file, delimiter=",")
        data_writer.writerow(headers)  # write headers
        data_writer.writerows(data)  # write all data


def write_dicts_to_json(data, output_file):
    """
    :param data: list of {} or {}
        Data to write
    :param output_file: str
        Path to output file
    :return: void
        Saves output file as .json
    """

    with open(output_file, "w") as out:
        json.dump(
            data,  # data
            out,  # file handler
            indent=4, sort_keys=True  # pretty print
        )
