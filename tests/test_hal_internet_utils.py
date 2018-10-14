# -*- coding: utf-8 -*-


"""Tests hal.internet.utils implementation"""

from hal.internet.utils import is_internet_on, get_my_external_ip, \
    wait_until_internet


def test_add_params_to_url():
    """Tests hal.internet.utils.add_params_to_url method"""

    pass  # todo auto generated method stub


def test_is_internet_on():
    """Tests hal.internet.utils.is_internet_on method"""

    assert is_internet_on()


def test_wait_until_internet():
    """Tests hal.internet.utils.wait_until_internet method"""

    if is_internet_on():
        assert wait_until_internet()


def test_get_my_external_ip():
    """Tests hal.internet.utils.dget_my_external_ip method"""

    if is_internet_on():
        assert get_my_external_ip() is not None
