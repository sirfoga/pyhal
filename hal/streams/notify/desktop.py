# -*- coding: utf-8 -*-

"""Sends desktop notify with notify-send tool """

import subprocess


def send_notification(app_name, message):
    """Shows notify to screen

    :param app_name: Name of app to show
    :param message: Details of app to show
    """
    subprocess.call([
        "notify-send",
        str(app_name),
        str(message)
    ])
