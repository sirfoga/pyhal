# -*- coding: utf-8 -*-

""" Internet tools """

import socket
import urllib.parse as urlparse
from urllib.parse import urlencode

from hal import times
from hal.wrappers.errors import true_false_returns


def add_params_to_url(url, params):
    """Adds params to url
    :param url: Url
    :param params: Params to add
    :returns: original url with new params
    """
    url_parts = list(urlparse.urlparse(url))  # get url parts
    query = dict(urlparse.parse_qsl(url_parts[4]))  # get url query
    query.update(params)  # add new params
    url_parts[4] = urlencode(query)
    return urlparse.urlunparse(url_parts)


@true_false_returns
def is_internet_on(host="8.8.8.8", port=53, timeout=3):
    """

    :param host: str
    :param Google: public
    :param port: int
    :param 53: tcp
    :param timeout: int
    :param Seconds: Default value
    :returns: bool
      True iff machine has internet connection
    """

    socket.setdefaulttimeout(timeout)
    socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))


def wait_until_internet(time_between_attempts=3, max_attempts=10):
    """
    :param time_between_attempts: int
    :param Seconds: between 2 consecutive attempts
    :param max_attempts: int
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
