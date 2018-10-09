# -*- coding: utf-8 -*-
""" Email creator utils """


def get_email_content(file_path):
    """
    :param file_path: str
    :param Path: to file with email text
    :returns: str
      Email text (html formatted)
    """
    with open(file_path, "r") as in_file:
        text = str(in_file.read())
        return text.replace("\n", "<br>")
