# -*- coding: utf-8 -*-

"""Internet tools """

import socket
import time
import urllib.parse as urlparse
from urllib.parse import urlencode

import requests

from hal.wrappers.errors import true_false_returns, none_returns


def add_params_to_url(url, params):
    """Adds params to url

    :param url: Url
    :param params: Params to add
    :return: original url with new params
    """
    url_parts = list(urlparse.urlparse(url))  # get url parts
    query = dict(urlparse.parse_qsl(url_parts[4]))  # get url query
    query.update(params)  # add new params
    url_parts[4] = urlencode(query)
    return urlparse.urlunparse(url_parts)


@true_false_returns
def is_internet_on(host="8.8.8.8", port=53, timeout=3):
    """Checks if machine has internet connection

    :param host: hostname to test
    :param port: port of hostname
    :param timeout: seconds before discarding connection
    :return: True iff machine has internet connection
    """
    socket.setdefaulttimeout(timeout)
    socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))


def wait_until_internet(time_between_attempts=3, max_attempts=10):
    """Waits until machine has internet

    :param time_between_attempts: seconds between 2 consecutive attempts
    :param max_attempts: max number of attempts to try
    :return: True iff there is internet connection
    """
    counter = 0
    while not is_internet_on():
        time.sleep(time_between_attempts)  # wait until internet is on
        counter += 1

        if counter > max_attempts:
            return False

    return True


@none_returns
def get_my_external_ip():
    """Gets external IP

    :return: external IP
    """

    resp = requests.get(url="https://jsonip.com/")
    data = resp.json()
    return data["ip"]
