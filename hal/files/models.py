# !/usr/bin/python
# coding: utf_8

# Copyright 2016 Stefano Fogarollo
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


""" Main entities in files, such as documents, folders. """


import os
from hal.files.manager import is_hidden


class Document:
    @staticmethod
    def move_file_to_directory(file_path, directory_path):
        """
        :param file_path: string
            Path to file to move
        :param directory_path: string
            Path to target directory where to move file
        :return: void
            Move file to given directory
        """

        file_name = os.path.basename(file_path)  # get name of file
        if not os.path.exists(directory_path):
            os.makedirs(directory_path)  # create directory if necessary
        os.rename(file_path, os.path.join(directory_path, file_name))  # move file to location

    @staticmethod
    def move_file_to_file(old_path, new_path):
        """
        :param old_path: string
            Old path of file to move
        :param new_path: string
            New path (location) of file
        :return: void
            Move file from old location to new one
        """

        try:
            os.rename(old_path, new_path)
        except:
            old_file = os.path.basename(old_path)
            target_directory, target_file = os.path.dirname(os.path.abspath(new_path)), os.path.basename(new_path)
            try:
                Document.move_file_to_directory(
                    old_path,
                    target_directory
                )  # move old file to new directory then change name ot new name
                os.rename(os.path.join(target_directory, old_file), os.path.join(target_directory, target_file))
            except:
                print("[CRITICAL]", "Failed renaming", old_path, ">>", new_path)

    @staticmethod
    def write_data_to_file(data, out_file):
        """
        :param data: string
            Data to write to file.
        :param out_file: string
            Path to output file.
        :return: void
            Writes given data to given path file.
        """

        with open(out_file, "w") as f:
            f.write(data)

    @staticmethod
    def extract_name_extension(file_name):
        """
        :param file_name: string
            Name of file
        :return: tuple string, string
            Name of file, extension of file
        """

        return os.path.splitext(file_name)


class Directory:
    @staticmethod
    def ls_dir(path, include_hidden=False):
        """
        :param path: string
            Path to directory to get list of files and folders
        :param include_hidden: bool
            Whether to include hidden files in list.
        :return: list
            List of paths in given directory.
        """

        list_ = []
        for f in os.listdir(path):
            if include_hidden or not is_hidden(f):
                list_.append(os.path.join(path, f))
        return list_

    @staticmethod
    def ls_recurse(path, include_hidden=False):
        """
        :param path: string
            Path to directory to get list of files and folders
        :param include_hidden: bool
            Whether to include hidden files in list.
        :return: list
            List of paths in given directory recursively.
        """

        list_ = []
        for f in os.listdir(path):
            if include_hidden or not is_hidden(f):
                list_.append(os.path.join(path, f))
                if os.path.isdir(os.path.join(path, f)):
                    list_ += Directory.ls_recurse(os.path.join(path, f),
                                        include_hidden=include_hidden)  # get list of files in directory
        return list_

    @staticmethod
    def ls(path, recurse, include_hidden=False):
        """
        :param path: string
            Path to directory to get list of files and folders
        :param recurse: bool
            Whether to recurse into subdirectories or not.
        :param include_hidden: bool
            Whether to include hidden files in list.
        :return: list
            List of paths in given directory recursively.
        """

        if recurse:
            return Directory.ls_recurse(path, include_hidden=include_hidden)
        else:
            return Directory.ls_dir(path, include_hidden=include_hidden)
