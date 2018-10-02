# !/usr/bin/python3
# coding: utf-8


""" Internet tools """

import socket
import urllib.parse as urlparse
from urllib.parse import urlencode

import times


def add_params_to_url(url, params):
    """
    :param url: str
        Url to add params to
    :param params: {}
        List of params to add to url
    :return: void
        Adds params to url
    """

    url_parts = list(urlparse.urlparse(url))  # get url parts
    query = dict(urlparse.parse_qsl(url_parts[4]))  # get url query
    query.update(params)  # add new params
    url_parts[4] = urlencode(query)
    return urlparse.urlunparse(url_parts)


def is_internet_on(host="8.8.8.8", port=53, timeout=3):
    """
    :param host: str
        Google-public-dns-a.google.com
    :param port: int
        53/tcp
    :param timeout: int
        Seconds
    :return: bool
        True iff machine has internet connection
    """

    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return True
    except:
        return False


def wait_until_internet(time_between_attempts=3, max_attempts=10):
    """
    :param time_between_attempts: int
        Seconds between 2 consecutive attempts
    :param max_attempts: int
        Max number of attempts to try
    :return: bool
        True iff there is internet connection
    """

    counter = 0
    while not is_internet_on():
        times.sleep(time_between_attempts)  # wait until internet is on
        counter += 1

        if counter > max_attempts:
            return False

    return True
