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
import re

from mutagen.id3 import ID3
from mutagen.id3._frames import TIT2, TPE1, TALB, TRCK, TDRC
from mutagen.mp3 import MP3
from send2trash import send2trash

BAD_CHARS = [
    ".", ":", "\"", "’", "&", "720p", "1080p", "yify", ",", "\"S", "brrip", "bluray", "Bokutox", "x264", "[", "]", "sparks", "h264",
    "aac", "ozlem", "ac3", "ozlem", "etrg", "dvdrip", "xvid", "nydic", "sujaidr", "x265", "hevc", "(pimprg)", "aac",
    "ozlem", "remastered", "anoxmous", "yts"]  # official formats based on wikipedia
RUSSIAN_CHARS = ["ш", "а", "б", "л", "о", "н", "ы", "р", "е", "а", "л", "и", "з", "а", "ц", "и", "и", "к",
    "о", "р", "п", "о", "р", "а", "т", "и", "в", "н", "ы", "х", "п", "р", "и", "л", "о", "ж", "е", "н", "и", "й",
    "в", "о", "п", "р", "о", "с", "ы", "и", "о", "т", "в", "е", "т", "ы", "п", "о", "б", "е", "з", "о", "п",
    "а", "с", "н", "о", "с", "т", "и", "д", "а", "н", "н", "ы", "х"]
VIDEO_FORMAT = [".", ".3g2", ".3gp", ".amv", ".asf", ".avi", ".drc", ".f4a", ".f4b", ".f4p", ".f4v", ".flv",
    ".gifv", ".m2v", ".m4p", ".m4v", ".mkv", ".mng", ".mov", ".mp2", ".mp4", ".mpe", ".mpeg", ".mpg", ".mpv", ".mxf",
    ".nsv", ".ogg", ".ogv", ".qt", ".rm", ".rmvb", ".roq", ".svi", ".vob", ".webm", ".wmv", ".yuv"]
ARCHIVE_FORMAT = [".7z", ".??_", ".?Q?", ".?Z?", ".a", ".ace", ".afa", ".alz", ".apk", ".ar", ".arc", ".arj",
                      ".b1", ".ba", ".bh", ".bz2", ".cab", ".car", ".cfs", ".cpio", ".cpt", ".dar", ".dd", ".dgc",
                      ".dmg", ".ear", ".ecc", ".F", ".gca", ".gz", ".ha", ".hki", ".ice", ".infl", ".iso", ".jar",
                      ".kgb", ".LBR", ".lbr", ".lha", ".lz", ".lzh", ".lzma", ".lzo", ".lzx", ".mar", ".pak", ".paq6",
                      ".paq7", ".paq8", ".par", ".par2", ".partimg", ".pea", ".pim", ".pit", ".qda", ".rar", ".rk",
                      ".rz", ".s7z", ".sda", ".sea", ".sen", ".sfark", ".sfx", ".shar", ".shk", ".sit", ".sitx",
                      ".sqx", ".sz", ".tar", ".tar.bz2", ".tar.gz", ".tar.lzma", ".tar.Z", ".tbz2", ".tgz", ".tlz",
                      ".uc", ".uc0", ".uc2", ".uca", ".ucn", ".ue2", ".uha", ".ur2", ".war", ".wim", ".xar", ".xp3",
                      ".xz", ".yz1", ".z", ".Z", ".zip", ".zipx", ".zoo", ".zpaq", ".zz"]
SUBTITLE_FORMAT = [".srt", ".sub", ".sbv"]
TEXT_FORMAT = [".cnf", ".conf", ".cfg", ".chm", ".epub", ".log", ".asc", ".txt", ".url"]
IMAGE_FORMAT = [".ani", ".bmp", ".cal", ".fax", ".gif", ".img", ".jbg", ".jpe", ".jpe", ".jpg", ".mac", ".pbm",
                ".pcd", ".pcx", ".pct", ".pgm", ".png", ".ppm", ".psd", ".ras", ".tga", ".tif", ".wmf"]
AUDIO_FORMAT = [".3gp", ".aa", ".aac", ".aax", ".act", ".aiff", ".amr", ".ape", ".au", ".awb", ".dct", ".dss", ".dvf",
                ".flac", ".gsm", ".iklax", ".ivs", ".m4a", ".m4b", ".m4p", ".mmf", ".mogg", ".mp3", ".mpc", ".msv",
                ".oga", ".ogg", ".opus", ".ra", ".raw", ".rm", ".sln", ".tta", ".vox", ".wav", ".webm", ".wma", ".wv"]


class FileSystem(object):
    def __init__(self, path):
        """
        :param path: string
            Path to file
        """
        object.__init__(self)

        self.path = path
        self.name, extension = os.path.splitext(self.path)

    @staticmethod
    def fix_raw_path(path):
        """
        :param path: string
            Path to fix
        :return: string
            Right path
        """

        if os.path.isdir(path):
            if not path.endswith("/"):
                return path + "/"
            else:
                return path
        else:
            return path

    @staticmethod
    def remove_year(name):
        """
        :param name: string
            Name to edit
        :return: string
            Given string bu with no years.
        """

        l_bracket, r_bracket = name.find("("), name.find(")")  # find limits of year
        if r_bracket - l_bracket + 1 == 6:  # there is a year in between
            name = name.replace(name[l_bracket: r_bracket + 1], "")  # remove year
        else:
            l_bracket, r_bracket = name.find("["), name.find("]")  # try with square brackets
            if r_bracket - l_bracket + 1 == 6:  # there is a year in between
                name = name.replace(name[l_bracket: r_bracket + 1], "")  # remove year
            else:
                name = name

        for i in range(len(name) - 4):
            try:
                if name[i: i + 4].isdigit():
                    name = name[:i] + name[i + 4:]
            except:  # out of bounds
                pass

        return name

    @staticmethod
    def remove_brackets(name):
        """
        :param name: string
            Name to edit
        :return: string
            Given string bu with no barckets.
        """

        name = re.sub("([\(\[]).*?([\)\]])", "\g<1>\g<2>", name)
        name = name.replace("()", "")  # remove anything in ()
        if name.rfind("(") > 0:  # there exists a "("
            name = name[:name.rfind("(")]
        name = name.replace("(", "")
        name = name.replace(")", "")
        for _ in range(10):
            name = name.replace("  ", " ")  # remove extra blanks
        name = name.strip()
        return name

    @staticmethod
    def extract_name_max_chars(name, max_chars, blank=" "):
        """
        :param name: string
            Name to edit
        :param max_chars: int
            Maximum chars of new name
        :param blank: string
            Char that represents the blank between words.
        :return: string
            Name edited to contain at most max_chars (truncate to nearest word)
        """

        if len(name) > max_chars:
            new_name = name[:max_chars]  # get at most 64 chars
            if new_name.rfind(blank) > 0:
                new_name = new_name[:new_name.rfind(blank)]  # truncate to nearest word
            return new_name
        else:
            return name

    @staticmethod
    def prettify(name, bad_chars=BAD_CHARS, r=" "):
        """
        :param name: string
            Name to edit
        :param bad_chars: []
            List of bad strings to remove
        :param r: string
            Default blanks in name.
        :return: string
            Prettier name from given one: replace bad chars with good ones.
        """

        if name.startswith("."):  # remove starting .
            name = name[1:]

        for t in bad_chars:
            name = name.replace(t.lower(), r)  # remove token
        name = name.replace(" ", r)  # replace blanks
        while name.find(r + r) >= 0:  # while there are blanks to remove
            name = name.replace(r + r, r)

        for i in range(1, len(name) - 2):  # loop through characters except 1 and end
            try:
                if name[i - 1] == r and name[i + 1] == r and name[i] in bad_chars:  # 2 blanks hug one bad char
                    name = name[:i - 1] + name[i + 2:]
            except:  # out of bounds
                pass

        if name.endswith(r):  # remove ending replacement
            name = name[:-1]

        return name

    def is_archive_mac(self):
        """
        :return: True iff document is an MACOSX archive.
        """

        return "macosx" in self.path.lower()

    def is_russian(self):
        """
        :return: True iff document has a russian name.
        """

        russian_chars = 0
        for c in RUSSIAN_CHARS:
            if c in self.name:
                russian_chars += 1  # found a russian char
        return russian_chars > len(RUSSIAN_CHARS) / 2.0

    def trash(self):
        """
        :return: void
            Trash given file/folder
        """

        send2trash(self.path)

    def rename(self, new_path):
        """
        :param new_path: string
            New path to use
        :return: void
            Rename to new path
        """

        rename_path = self.fix_raw_path(new_path)
        if os.path.isdir(self.path):
            os.rename(self.path, rename_path)
        else:
            os.renames(self.path, rename_path)


class Document(FileSystem):
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

    def get_path_name(self):
        """
        :return: tuple string, string
            Name of path, name of file (or folder)
        """

        path = self.fix_raw_path(os.path.dirname(os.path.abspath(self.path)))
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

    def is_hidden(self):
        """
        :return: bool
            True iff path is hidden
        """

        hidden_start_path = "/."
        return hidden_start_path in self.path


class Directory(FileSystem):
    def __init__(self, path):
        """
        :param path: string
            Path to file
        """

        FileSystem.__init__(self, self.fix_raw_path(path))

        self.root_path, self.name = self.get_path_name()

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
            if include_hidden or not Document(f).is_hidden():
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
            if include_hidden or not Document(f).is_hidden():
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

        p = os.path.dirname(os.path.abspath(self.path))
        name = self.path.replace(p + "/", "")[: -1]  # replace in full path, dir path to get name
        return p, name

    def is_empty(self):
        """
        :return: Bool
            True iff empty
        """

        return not os.listdir(self.path)


class MP3Song(FileSystem):
    """ mp3 song """

    def __init__(self, path):
        FileSystem.__init__(self, path)

        self.song = MP3(self.path, ID3=ID3)
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
        self.tags.add(TRCK(encoding=3, text=str(nr_track)))
        self.song.save()

    def set_year(self, year):
        self.tags.add(TDRC(encoding=3, text=str(year)))
        self.song.save()
