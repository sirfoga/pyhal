# !/usr/bin/python3
# coding: utf-8


""" Documents and folders in system """

import os

from hal.files.models.system import FileSystem
from hal.files.models.system import VIDEO_FORMAT, SUBTITLE_FORMAT, \
    TEXT_FORMAT, IMAGE_FORMAT, AUDIO_FORMAT, PATH_SEPARATOR
from hal.files.models.system import fix_raw_path


class Document(FileSystem):
    """ File with content in a OS """

    def __init__(self, path):
        """
        :param path: string
            Path to file
        """

        FileSystem.__init__(self, path)

        self.root_path, self.full_name = self.get_path_name()
        self.name, self.extension = os.path.splitext(self.full_name)

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
        os.rename(file_path, os.path.join(directory_path,
                                          file_name))  # move file to location

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
            target_directory, target_file = os.path.dirname(
                os.path.abspath(new_path)), os.path.basename(new_path)
            try:
                Document.move_file_to_directory(
                    old_path,
                    target_directory
                )  # move old file to new directory, change name to new name
                os.rename(os.path.join(target_directory, old_file),
                          os.path.join(target_directory, target_file))
            except:
                print("[CRITICAL]", "Failed renaming", old_path, ">>",
                      new_path)

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

        with open(out_file, "w") as out_f:
            out_f.write(data)

    @staticmethod
    def extract_name_extension(file_name):
        """
        :param file_name: string
            Name of file
        :return: tuple string, string
            Name of file, extension of file
        """
        return os.path.splitext(file_name)

    def get_path_name(self):
        """
        :return: tuple string, string
            Name of path, name of file (or folder)
        """

        path = fix_raw_path(os.path.dirname(os.path.abspath(self.path)))
        name = os.path.basename(self.path)
        return path, name

    def is_video(self):
        """
        :return: True iff document is a video.
        """
        return self.extension.lower() in VIDEO_FORMAT

    def is_subtitle(self):
        """
        :return: True iff document is a subtitle.
        """

        return self.extension.lower() in SUBTITLE_FORMAT

    def is_text(self):
        """
        :return: True iff document is a text file.
        """

        return self.extension.lower() in TEXT_FORMAT

    def is_image(self):
        """
        :return: True iff document is an image.
        """

        return self.extension.lower() in IMAGE_FORMAT

    def is_audio(self):
        """
        :return: True iff document is an audio.
        """

        return self.extension.lower() in AUDIO_FORMAT


class Directory(FileSystem):
    """ Folder of a OS """

    def __init__(self, path):
        """
        :param path: string
            Path to file
        """

        FileSystem.__init__(self, fix_raw_path(path))

        self.root_path, self.name = self.get_path_name()

    @staticmethod
    def create_new(path):
        """
        :param path: string
            Path to directory to create
        :return: void
            Creates new directory
        """

        if not os.path.exists(path):
            os.makedirs(path)

    def get_path_name(self):
        """
        :return: tuple string, string
            Name of path, name of file (or folder)
        """

        complete_path = os.path.dirname(os.path.abspath(self.path))
        name = self.path.replace(complete_path + PATH_SEPARATOR, "")
        if name.endswith("/"):
            name = name[: -1]

        return complete_path, name

    def is_empty(self):
        """
        :return: Bool
            True iff empty
        """

        return not os.listdir(self.path)
