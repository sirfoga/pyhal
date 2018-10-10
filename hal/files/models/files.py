# -*- coding: utf-8 -*-

"""Documents and folders in system """

import os

from hal.files.models.system import FileSystem
from hal.files.models.system import VIDEO_FORMAT, SUBTITLE_FORMAT, \
    TEXT_FORMAT, IMAGE_FORMAT, AUDIO_FORMAT, PATH_SEPARATOR
from hal.files.models.system import fix_raw_path


class Document(FileSystem):
    """File with content in a OS"""

    def __init__(self, path):
        """
        :param path: Path to file
        """
        super().__init__(path)
        self.root_path, self.full_name = self.get_path_name()
        self.name, self.extension = os.path.splitext(self.full_name)

    @staticmethod
    def move_file_to_directory(file_path, directory_path):
        """Moves file to given directory

        :param file_path: path to file to move
        :param directory_path: path to target directory where to move file
        """
        file_name = os.path.basename(file_path)  # get name of file
        if not os.path.exists(directory_path):
            os.makedirs(directory_path)  # create directory if necessary
        os.rename(file_path, os.path.join(directory_path,
                                          file_name))  # move file to location

    @staticmethod
    def move_file_to_file(old_path, new_path):
        """Moves file from old location to new one

        :param old_path: path of file to move
        :param new_path: new path
        """
        try:
            os.rename(old_path, new_path)
        except:
            old_file = os.path.basename(old_path)
            target_directory, target_file = os.path.dirname(
                os.path.abspath(new_path)), os.path.basename(new_path)
            Document.move_file_to_directory(
                old_path,
                target_directory
            )  # move old file to new directory, change name to new name
            os.rename(os.path.join(target_directory, old_file),
                      os.path.join(target_directory, target_file))

    @staticmethod
    def write_data_to_file(data, out_file):
        """Writes given data to given path file

        :param data: data to write to file
        :param out_file: path to output file
        """
        with open(out_file, "w") as out_f:
            out_f.write(data)

    @staticmethod
    def extract_name_extension(file_name):
        """Gets name and extension of file

        :param file_name: Name of file
        :returns: Name of file, extension of file
        """
        return os.path.splitext(file_name)

    def get_path_name(self):
        """Gets path and name of song

        :returns: Name of path, name of file (or folder)
        """
        path = fix_raw_path(os.path.dirname(os.path.abspath(self.path)))
        name = os.path.basename(self.path)
        return path, name

    def is_video(self):
        """Checks if file is video

        :returns: True iff document is a video.
        """
        return self.extension.lower() in VIDEO_FORMAT

    def is_subtitle(self):
        """Checks if file is subtitle

        :returns: True iff document is a subtitle.
        """

        return self.extension.lower() in SUBTITLE_FORMAT

    def is_text(self):
        """Checks if file is text

        :returns: True iff document is a text file.
        """

        return self.extension.lower() in TEXT_FORMAT

    def is_image(self):
        """Checks if file is image

        :returns: True iff document is an image.
        """

        return self.extension.lower() in IMAGE_FORMAT

    def is_audio(self):
        """Checks if file is audio

        :returns: True iff document is an audio.
        """

        return self.extension.lower() in AUDIO_FORMAT


class Directory(FileSystem):
    """Folder of a OS"""

    def __init__(self, path):
        """
        :param path: Path to file
        """
        super().__init__(fix_raw_path(path))
        self.root_path, self.name = self.get_path_name()

    @staticmethod
    def create_new(path):
        """Creates new directory

        :param path: path to directory to create
        """
        if not os.path.exists(path):
            os.makedirs(path)

    def get_path_name(self):
        """Gets path and name of file

        :returns: Name of path, name of file (or folder)
        """
        complete_path = os.path.dirname(os.path.abspath(self.path))
        name = self.path.replace(complete_path + PATH_SEPARATOR, "")
        if name.endswith("/"):
            name = name[: -1]

        return complete_path, name

    def is_empty(self):
        """Checks if folder is empty

        :returns: BTrue iff empty
        """
        return not os.listdir(self.path)
