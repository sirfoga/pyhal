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


""" file manager """

import errno
import os
import random
import shutil

from mutagen.id3 import ID3
from mutagen.mp3 import MP3
from send2trash import send2trash


class Folder(object):
    """ abstract representation of folder """

    def __init__(self, path):
        if os.path.exists(path):
            object.__init__(self)
            self.path = path
        else:
            self.path = os.getcwd()  # get current directory

    def __str__(self):
        return str(self.path)

    def have_equal_struct(self, other):
        """
        :param other: other istance of Folder
        :return: True iff have same folder structures
        """

        assert(type(self) == type(other))  # check if same class
        return self.view_folders() == other.view_folders()

    def visual(self):
        """
        :return: visual representation of tree structure
        """

        return str(self) + '/\n' + self.view_all(self.path)

    def view_folders(self, path):
        """
        :param path: path to folder
        :return: string representation of folder structure
        """

        content = []
        cont = os.listdir(path)  # first print files
        dirs = []
        for doc in cont:
            if os.path.isdir(os.path.join(path, doc)):
                dirs.append(doc)
        dirs.sort()
        cont = dirs

        for index in range(len(cont)):
            if os.path.isdir(os.path.join(path, cont[index])):
                if not index == len(cont) - 1:
                    content.append('├── ' + str(cont[index]) + '/\n')
                else:
                    content.append('└── ' + str(cont[index]) + '/\n')

                sub_content = self.view_folders(os.path.join(path, cont[index]))
                lines = sub_content.split('\n')

                if not index == len(cont) - 1:
                    for line in lines:
                        if len(line) > 0:
                            content.append('│   ' + line + '\n')
                else:
                    for line in lines:
                        if len(line) > 0:
                            content.append('    ' + line + '\n')

        return ''.join(content)

    def view_all(self, path):
        """
        :param path: path to directory to print
        :return: get directory content (recursively)
        """

        content = []
        cont = os.listdir(path)  # first print file
        files = []
        dirs = []
        for doc in cont:
            if os.path.isdir(os.path.join(path, doc)):
                dirs.append(doc)
            else:
                files.append(doc)
        files.sort()
        dirs.sort()
        files.extend(dirs)
        cont = files

        for index in range(len(cont)):
            if not os.path.isdir(os.path.join(path, cont[index])):
                if not index == len(cont) - 1:
                    content.append('├── ' + str(cont[index]) + '\n')
                else:  # last object
                    content.append('└── ' + str(cont[index]) + '\n')

        # then folders
        for index in range(len(cont)):
            if os.path.isdir(os.path.join(path, cont[index])):
                if not index == len(cont) - 1:
                    content.append('├── ' + str(cont[index]) + '/\n')
                else:
                    content.append('└── ' + str(cont[index]) + '/\n')

                sub_content = self.view_all(os.path.join(path, cont[index]))
                lines = sub_content.split('\n')

                if not index == len(cont) - 1:
                    for line in lines:
                        if len(line) > 0:
                            content.append('│   ' + line + '\n')
                else:
                    for line in lines:
                        if len(line) > 0:
                            content.append('    ' + line + '\n')

        return ''.join(content)

    @staticmethod
    def new(path):
        """
        :param path: where to create folder
        :return: creates folder with given name in given directory
        """

        try:
            os.makedirs(path)
        except:
            raise ValueError("Cannot create new directory \"" + path + "\"")

    @staticmethod
    def trash(path):
        """
        :param path: path to directory to trash
        :return: move to trash directory
        """
        try:
            send2trash(path)
        except:
            raise ValueError("Cannot trash directory \"" + path + "\"")

    @staticmethod
    def rename(old_path, old_name, new_name):
        """
        :param old_path: location of folder to rename
        :param old_name: name of folder to rename
        :param new_name: new name
        :return: rename folder
        """

        os.rename(os.path.join(old_path, old_name), os.path.join(old_path, new_name))


class Document(object):
    """ file/document """

    def __init__(self):
        object.__init__(self)

    @staticmethod
    def new(file_data, file_name, file_path):
        """
        :param file_data: data to write in file
        :param file_name: name of new file
        :param file_path: path to file
        :return: new file with name and path given
        """

        try:
            f = open(os.path.join(file_path, file_name), 'w')
            f.write(file_data)
            f.close()
            return True
        except:
            try:
                Folder.new(file_path)
                f = open(os.path.join(file_path, file_name), 'w')
                f.write(file_data)
                f.close()
                return True
            except:
                return False

    @staticmethod
    def random(minchar, maxchar, minlen, maxlen, wordamount):
        """
        :param minchar: minimum char allowed in each word (0 .. 9 : ; < = > ? @ A .. Z [ \ ] ^_ ` a .. z)
        :param maxchar: maximum char allowed in each word
        :param minlen: minimum length of words
        :param maxlen: maximum length of words
        :param wordamount: amount of words per document
        :return: string of given size and parameters
        """

        out_string = ""
        for word in range(0, wordamount):
            num_char = random.randrange(minlen, maxlen)  # number of char in word
            new_word = ""  # create new word
            for char in range(0, num_char):
                new_word += chr(random.randrange(ord(minchar), ord(maxchar)))

            out_string = out_string + new_word + " "

        return out_string

    @staticmethod
    def trash(path):
        """
        :param path: path to file to trash
        :return: trash given file
        """

        os.remove(path)

    @staticmethod
    def write_lines_file(array, file_name, file_path):
        """
        :param array: array to join
        :param file_name: name of file to write
        :param file_path: path to file
        :return: new file with name and array given
        """

        file_data = ''.join(array)
        return Document.new_file(file_data, file_name, file_path)

    @staticmethod
    def read_file(file_name):
        """
        :param file_name: path of file to open
        :return: file content
        """

        f = open(file_name)
        file_data = f.read()
        f.close()
        return file_data

    @staticmethod
    def read_lines_file(file_name):
        """
        :param file_name: name of file to open
        :return: file lines in array
        """

        return [line.rstrip('\n') for line in open(file_name)]

    @staticmethod
    def copy(src, dest):
        """
        :param src: source directory to be copied in..
        :param dest: ..destination directory
        :return: copy src dir to dest dir
        """

        try:
            shutil.copytree(src, dest)
        except OSError as e:
            # If the error was caused because the source wasn't a directory
            if e.errno == errno.ENOTDIR:
                shutil.copy(src, dest)
            else:
                raise ValueError('Failed copying ' + str(src) + ' to ' + str(dest) + '\n' + str(e))

    @staticmethod
    def rename(old_path, old_name, new_name):
        """
        :param old_path: location of file to rename
        :param old_name: name of file to rename
        :param new_name: new name
        :return: rename file
        """

        os.rename(os.path.join(old_path, old_name), os.path.join(old_path, new_name))

    @staticmethod
    def search_file(name, start_path):
        """
        :param name: name of file to be searched
        :param start_path: start searching from here
        :return: array of paths containing files named like given name
        """

        search_result = []

        for root, subdirs, files in os.walk(start_path, topdown=False):
            for doc in files:
                filename = str(doc.split('.')[0])
                if name in filename:
                    search_result.append(os.path.join(root, doc))

        return search_result

    @staticmethod
    def are_psame(src_address, dest_address, maximum_access_time_delta):
        """
        :param src_address: first file
        :param dest_address: second file
        :return: True if are *probably* same file
        """

        stat_src = os.stat(src_address)
        stat_dest = os.stat(dest_address)
        if stat_src.st_mode == stat_dest.st_mode and stat_src.st_size == stat_dest.st_size or abs(stat_src.st_atime - stat_dest.st_atime) < maximum_access_time_delta:
            return True
        else:
            return False


class MP3Song(object):
    """ mp3 song """
    
    def __init__(self, path):
        object.__init__(self)

        self.path = path
        self.song = MP3(this.path, ID3=ID3)
        self.tags = self.song.tags

    def set_name(self, name):
        self.tags.add(TIT2(encoding=3, text=name.decode('utf-8')))
        self.song.save()

    def set_artist(self, artist):
        self.tags.add(TPE1(encoding=3, text=artist.decode('utf-8')))
        self.song.save()

    def set_album(self, album):
        self.tags.add(TALB(encoding=3, text=album.decode('utf-8')))
        self.song.save()

    def set_nr_track(self, nr_track):
        self.tags.add(TRCK(encoding=3, text=str(nr_track).decode()))
        self.song.save()

    def set_year(self, year):
        self.tags.add(TDRC(encoding=3, text=str(year).decode()))
        self.song.save()
