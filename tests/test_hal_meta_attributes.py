# -*- coding: utf-8 -*-


"""Tests hal.meta.attributes implementation"""

import os

from hal.meta.attributes import ModuleFile, get_method_name, get_class_name
from hal.meta.attributes import get_modules

HERE = os.path.abspath(os.path.dirname(__file__))
ROOT_MODULE = os.path.join(os.path.dirname(HERE), "hal")  # hal sources
TEST_MODULE = os.path.join(ROOT_MODULE, "charts", "models.py")  # charts


def test__get_modules():
    """Tests hal.meta.attributes._get_modules method"""

    pass  # todo auto generated method stub


def test_get_modules():
    """Tests hal.meta.attributes.get_modules method"""

    hal_src = ROOT_MODULE
    modules = get_modules(hal_src)

    assert TEST_MODULE in modules

    meta_modules = get_modules(hal_src, include_meta=TEST_MODULE)
    meta_module = os.path.join(ROOT_MODULE, "__version__.py")
    assert meta_module in meta_modules
    assert meta_module not in modules


def test_get_class_name():
    """Tests hal.meta.attributes.get_class_name method"""
    assert get_class_name(None) == "NoneType"


def test_get_method_name():
    """Tests hal.meta.attributes.get_method_name method"""
    assert get_method_name(get_method_name) == "get_method_name"


class TestModuleFile:
    """Tests ModuleFile class"""

    @staticmethod
    def test__parse():
        """Tests hal.meta.attributes.ModuleFile._parse method"""

        pass  # todo auto generated method stub

    @staticmethod
    def test__find_package():
        """Tests hal.meta.attributes.ModuleFile._find_package method"""

        pass  # todo auto generated method stub

    @staticmethod
    def test_get_tree():
        """Tests hal.meta.attributes.ModuleFile.get_tree method"""

        f = ModuleFile(TEST_MODULE, ROOT_MODULE)
        assert f.package == "hal.charts.models"

        classes = f.get_tree().get_classes()
        assert len(classes) == 1

        assert classes[0].full_package == "hal.charts.models.SimpleChart"
        assert classes[0].get_functions()[1].full_package.startswith(
            "hal.charts.models.SimpleChart"
        )
        assert classes[0].get_functions(include_meta=True)[0].get_name() \
               == "__init__"
        assert len(classes[0].get_functions()) == 6

        functions = f.get_tree().get_functions()
        assert len(functions) == 0


class TestModuleTree:
    """Tests ModuleTree class"""

    @staticmethod
    def test__get_instances():
        """Tests hal.meta.attributes.ModuleTree._get_instances method"""

        pass  # todo auto generated method stub

    @staticmethod
    def test_get_classes():
        """Tests hal.meta.attributes.ModuleTree.get_classes method"""

        pass  # todo auto generated method stub

    @staticmethod
    def test_get_functions():
        """Tests hal.meta.attributes.ModuleTree.get_functions method"""

        pass  # todo auto generated method stub

    @staticmethod
    def test_get_name():
        """Tests hal.meta.attributes.ModuleTree.get_name method"""

        pass  # todo auto generated method stub


class TestModuleTreeObject:
    """Tests ModuleTreeObject class"""

    pass  # todo auto generated method stub


class TestPyClass:
    """Tests PyClass class"""

    @staticmethod
    def test_get_functions():
        """Tests hal.meta.attributes.PyClass.get_functions method"""

        pass  # todo auto generated method stub


class TestPyFunction:
    """Tests PyFunction class"""

    pass  # todo auto generated method stub
