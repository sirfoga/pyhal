# -*- coding: utf-8 -*-

""" Internet tools """

import socket
import urllib.parse as urlparse
from urllib.parse import urlencode

from hal import times


def add_params_to_url(url, params):
    """Arguments:
      url: str
    Url to add params to

    :param url:
    :param params:
    :returns: void
      Adds params to url
    """
    url_parts = list(urlparse.urlparse(url))  # get url parts
    query = dict(urlparse.parse_qsl(url_parts[4]))  # get url query
    query.update(params)  # add new params
    url_parts[4] = urlencode(query)
    return urlparse.urlunparse(url_parts)


def is_internet_on(host="8.8.8.8", port=53, timeout=3):
    """

    :param host: str (Default value = "8.8.8.8")
    :param Google: public
    :param port: int (Default value = 53)
    :param 53: tcp
    :param timeout: int (Default value = 3)
    :param Seconds: Default value
    :returns: bool
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

    :param time_between_attempts: int (Default value = 3)
    :param Seconds: between 2 consecutive attempts
    :param max_attempts: int (Default value = 10)
    :param Max: number of attempts to try
    :returns: bool
      True iff there is internet connection
    """
    counter = 0
    while not is_internet_on():
        times.sleep(time_between_attempts)  # wait until internet is on
        counter += 1

        if counter > max_attempts:
            return False

    return True
