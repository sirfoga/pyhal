# -*- coding: utf-8 -*-

"""Finds attributes of classes and functions in files"""

import ast
import os

from hal.files.models.system import get_folder_name

MODULE_SEP = "."


class File:
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

        return Tree(self.tree, root_package=self.package)


class Tree:
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


class TreeObject(Tree):
    """Object of Python tree"""

    def __init__(self, tree, root_package):
        super().__init__(tree, root_package)
        self.full_package = self.package + MODULE_SEP + self.get_name()


class PyClass(TreeObject):
    """Python parsed class"""

    def get_functions(self):
        """Finds top-level functions in file

        :return: list of top-level functions
        """
        instances = self._get_instances(ast.FunctionDef)
        instances = [
            PyFunction(instance, self.full_package)
            for instance in instances
        ]
        return instances


class PyFunction(TreeObject):
    """Python parsed method"""
