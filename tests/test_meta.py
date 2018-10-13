# !/usr/bin/python
# coding: utf_8


"""Tests meta module implementation"""

import os

from hal.meta.attributes import File

HERE = os.path.abspath(os.path.dirname(__file__))
ROOT_MODULE = os.path.join(os.path.dirname(HERE), "hal")  # hal sources
TEST_MODULE = os.path.join(ROOT_MODULE, "charts", "models.py")  # charts


class TestFile:
    """Tests File implementation"""

    def test_all(self):
        """Asserts all methods in File """

        f = File(TEST_MODULE, ROOT_MODULE)
        assert f.package == "hal.charts.models"

        classes = f.get_tree().get_classes()
        assert len(classes) == 1

        assert classes[0].full_package == "hal.charts.models.SimpleChart"
        assert classes[0].get_functions()[1].full_package == \
               "hal.charts.models.SimpleChart.setup"
        assert len(classes[0].get_functions()) == 7

        functions = f.get_tree().get_functions()
        assert len(functions) == 0
