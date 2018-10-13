# -*- coding: utf-8 -*-


"""Tests meta module implementation"""

import os

from hal.meta.attributes import ModuleFile, get_modules

HERE = os.path.abspath(os.path.dirname(__file__))
ROOT_MODULE = os.path.join(os.path.dirname(HERE), "hal")  # hal sources
TEST_MODULE = os.path.join(ROOT_MODULE, "charts", "models.py")  # charts


class TestAttributes:
    """Tests File implementation"""

    def test_all(self):
        """Asserts all methods in File """

        f = ModuleFile(TEST_MODULE, ROOT_MODULE)
        assert f.package == "hal.charts.models"

        classes = f.get_tree().get_classes()
        assert len(classes) == 1

        assert classes[0].full_package == "hal.charts.models.SimpleChart"
        assert classes[0].get_functions()[1].full_package == \
               "hal.charts.models.SimpleChart.setup"
        assert classes[0].get_functions()[0].get_name() == "__init__"
        assert len(classes[0].get_functions()) == 7

        functions = f.get_tree().get_functions()
        assert len(functions) == 0

    def test_get_modules(self):
        hal_src = ROOT_MODULE
        modules = get_modules(hal_src)

        assert TEST_MODULE in modules

        meta_modules = get_modules(hal_src, include_meta=TEST_MODULE)
        meta_module = os.path.join(ROOT_MODULE, "__version__.py")
        assert meta_module in meta_modules
        assert meta_module not in modules


class TestClass:
    @staticmethod
    def test_b():
        assert True


def test_a():
    assert True
