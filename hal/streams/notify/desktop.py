# !/usr/bin/python3
# coding: utf-8

""" Sends desktop notify with notify-send tool """

import subprocess


def send_notification(app_name, message):
    """
    :param app_name: str
        Name of app to show
    :param message: str
        Details of app to show
    :return: void
        Shows notify to screen
    """

    subprocess.call([
        "notify-send",
        str(app_name),
        str(message)
    ])
