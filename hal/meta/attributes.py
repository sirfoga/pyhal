# -*- coding: utf-8 -*-

"""Finds attributes of classes and functions in files"""

import ast
import os

from hal.files.models.files import Document
from hal.files.models.system import get_folder_name, is_file, \
    is_folder

MODULE_SEP = "."


class ModuleFile:
    """File attributes"""

    def __init__(self, path, root_package):
        """
        :param path: Path of file to parse
        """
        self.path = path
        self.package = self._find_package(root_package)
        self.tree = self._parse()

    def _parse(self):
        """Parses file contents

        :return: Tree hierarchy of file
        """
        with open(self.path, "rt") as reader:
            return ast.parse(reader.read(), filename=self.path)

    def _find_package(self, root_package):
        """Finds package name of file

        :param root_package: root package
        :return: package name
        """

        package = self.path.replace(root_package, "")
        if package.endswith(".py"):
            package = package[:-3]

        package = package.replace(os.path.sep, MODULE_SEP)
        root_package = get_folder_name(root_package)

        package = root_package + package  # add root
        return package

    def get_tree(self):
        """Finds tree hierarchy of file

        :return: Tree
        """

        return ModuleTree(self.tree, root_package=self.package)


class ModuleTree:
    """Hierarchy"""

    def __init__(self, tree, root_package):
        """
        :param tree: ast tree
        """
        self.tree = tree
        self.package = root_package

    def _get_instances(self, instance):
        """Finds all instances of instance in tree

        :param instance: type of object
        :return: list of objects in tree of same instance
        """

        return [
            x
            for x in self.tree.body
            if isinstance(x, instance)
        ]

    def get_classes(self):
        """Finds classes in file

        :return: list of top-level classes
        """
        instances = self._get_instances(ast.ClassDef)
        instances = [
            PyClass(instance, self.package)
            for instance in instances
        ]
        return instances

    def get_functions(self):
        """Finds top-level functions in file

        :return: list of top-level functions
        """
        instances = self._get_instances(ast.FunctionDef)
        instances = [
            PyFunction(instance, self.package)
            for instance in instances
        ]
        return instances

    def get_name(self):
        """Finds name of tree

        :return: name
        """
        return self.tree.name


class ModuleTreeObject(ModuleTree):
    """Object of Python tree"""

    def __init__(self, tree, root_package):
        super().__init__(tree, root_package)
        self.full_package = self.package + MODULE_SEP + self.get_name()


class PyClass(ModuleTreeObject):
    """Python parsed class"""

    def get_functions(self, include_meta=False):
        """Finds top-level functions in file

        :param include_meta: whether include meta functions like (__init__)
        :return: list of top-level functions
        """
        instances = self._get_instances(ast.FunctionDef)
        instances = [
            PyFunction(instance, self.full_package)  # fix package name
            for instance in instances
        ]

        if not include_meta:
            instances = [
                instance  # fix package name
                for instance in instances
                if not instance.get_name().startswith("__")
            ]

        return instances


class PyFunction(ModuleTreeObject):
    """Python parsed method"""


def _get_modules(path):
    """Finds modules in folder recursively

    :param path: directory
    :return: list of modules
    """
    lst = []
    folder_contents = os.listdir(path)
    is_python_module = "__init__.py" in folder_contents

    if is_python_module:
        for file in folder_contents:
            full_path = os.path.join(path, file)

            if is_file(full_path):
                lst.append(full_path)

            if is_folder(full_path):
                lst += _get_modules(full_path)  # recurse in folder

    return list(set(lst))


def get_modules(folder, include_meta=False):
    """Finds modules (recursively) in folder

    :param folder: root folder
    :param include_meta: whether include meta files like (__init__ or
        __version__)
    :return: list of modules
    """
    files = [
        file
        for file in _get_modules(folder)
        if is_file(file)  # just files
    ]

    if not include_meta:
        files = [
            file
            for file in files
            if not Document(file).name.startswith("__")
        ]

    return files


def get_class_name(obj):
    """Finds name of class of object

    :param obj: object
    :return: Name of class
    """
    return str(obj.__class__.__name__)
