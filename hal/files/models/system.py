# !/usr/bin/python3
# coding: utf-8


""" File system utils, renaming and parsing """

import os
import re

from send2trash import send2trash

BAD_CHARS = [
    ".", ":", "\"", "’", "&", "720p", "1080p", "yify", ",", "brrip", "bluray",
    "Bokutox", "x264", "[", "]", "sparks", "h264",
    "aac", "ozlem", "ac3", "ozlem", "etrg", "dvdrip", "xvid", "nydic",
    "sujaidr", "x265", "hevc", "(pimprg)", "aac",
    "ozlem", "remastered", "anoxmous",
    "yts"]  # official formats based on wikipedia
RUSSIAN_CHARS = ["ш", "а", "б", "л", "о", "н", "ы", "р", "е", "а", "л", "и",
                 "з", "а", "ц", "и", "и", "к",
                 "о", "р", "п", "о", "р", "а", "т", "и", "в", "н", "ы", "х",
                 "п", "р", "и", "л", "о", "ж", "е", "н", "и", "й",
                 "в", "о", "п", "р", "о", "с", "ы", "и", "о", "т", "в", "е",
                 "т", "ы", "п", "о", "б", "е", "з", "о", "п",
                 "а", "с", "н", "о", "с", "т", "и", "д", "а", "н", "н", "ы",
                 "х"]
VIDEO_FORMAT = [".", ".3g2", ".3gp", ".amv", ".asf", ".avi", ".drc", ".f4a",
                ".f4b", ".f4p", ".f4v", ".flv",
                ".gifv", ".m2v", ".m4p", ".m4v", ".mkv", ".mng", ".mov",
                ".mp2", ".mp4", ".mpe", ".mpeg", ".mpg", ".mpv", ".mxf",
                ".nsv", ".ogg", ".ogv", ".qt", ".rm", ".rmvb", ".roq", ".svi",
                ".vob", ".webm", ".wmv", ".yuv"]
ARCHIVE_FORMAT = [".7z", ".??_", ".?Q?", ".?Z?", ".a", ".ace", ".afa", ".alz",
                  ".apk", ".ar", ".arc", ".arj",
                  ".b1", ".ba", ".bh", ".bz2", ".cab", ".car", ".cfs", ".cpio",
                  ".cpt", ".dar", ".dd", ".dgc",
                  ".dmg", ".ear", ".ecc", ".F", ".gca", ".gz", ".ha", ".hki",
                  ".ice", ".infl", ".iso", ".jar",
                  ".kgb", ".LBR", ".lbr", ".lha", ".lz", ".lzh", ".lzma",
                  ".lzo", ".lzx", ".mar", ".pak", ".paq6",
                  ".paq7", ".paq8", ".par", ".par2", ".partimg", ".pea",
                  ".pim", ".pit", ".qda", ".rar", ".rk",
                  ".rz", ".s7z", ".sda", ".sea", ".sen", ".sfark", ".sfx",
                  ".shar", ".shk", ".sit", ".sitx",
                  ".sqx", ".sz", ".tar", ".tar.bz2", ".tar.gz", ".tar.lzma",
                  ".tar.Z", ".tbz2", ".tgz", ".tlz",
                  ".uc", ".uc0", ".uc2", ".uca", ".ucn", ".ue2", ".uha",
                  ".ur2", ".war", ".wim", ".xar", ".xp3",
                  ".xz", ".yz1", ".z", ".Z", ".zip", ".zipx", ".zoo", ".zpaq",
                  ".zz"]
SUBTITLE_FORMAT = [".srt", ".sub", ".sbv"]
TEXT_FORMAT = [".cnf", ".conf", ".cfg", ".chm", ".epub", ".log", ".asc",
               ".txt", ".url"]
IMAGE_FORMAT = [".ani", ".bmp", ".cal", ".fax", ".gif", ".img", ".jbg", ".jpe",
                ".jpe", ".jpg", ".mac", ".pbm",
                ".pcd", ".pcx", ".pct", ".pgm", ".png", ".ppm", ".psd", ".ras",
                ".tga", ".tif", ".wmf"]
AUDIO_FORMAT = [".3gp", ".aa", ".aac", ".aax", ".act", ".aiff", ".amr", ".ape",
                ".au", ".awb", ".dct", ".dss", ".dvf",
                ".flac", ".gsm", ".iklax", ".ivs", ".m4a", ".m4b", ".m4p",
                ".mmf", ".mogg", ".mp3", ".mpc", ".msv",
                ".oga", ".ogg", ".opus", ".ra", ".raw", ".rm", ".sln", ".tta",
                ".vox", ".wav", ".webm", ".wma", ".wv"]
PATH_SEPARATOR = "/" if "posix" in os.name else "\\"


def fix_raw_path(path):
    """
    :param path: string
        Path to fix
    :return: string
        Right path
    """

    double_path_separator = PATH_SEPARATOR + PATH_SEPARATOR
    while path.find(
            double_path_separator) >= 0:  # there are double separators
        path = path.replace(double_path_separator,
                            PATH_SEPARATOR)  # remove double path separator

    if is_folder(path) and not path.endswith("/"):
        path = path + "/"

    return path


def remove_year(name):
    """
    :param name: string
        Name to edit
    :return: string
        Given string bu with no years.
    """

    for i in range(len(
            name) - 3):  # last index is length - 3 - 1 = length - 4
        if name[i: i + 4].isdigit():
            name = name[:i] + name[i + 4:]
            return remove_year(
                name)  # if there is a removal, start again
    return name


def remove_brackets(name):
    """
    :param name: string
        Name to edit
    :return: string
        Given string bu with no brackets
    """

    name = re.sub(
        r"([(\[]).*?([)\]])",
        r"\g<1>\g<2>",
        name
    )  # remove anything in between brackets
    brackets = "()[]{}"  # list of brackets
    for bracket in brackets:
        name = name.replace(bracket, "")
    return name


def extract_name_max_chars(name, max_chars=64, blank=" "):
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

    if max_chars <= 0:
        raise ValueError(
            "Maximum chars of new name must be greater than 0")

    new_name = name.strip()
    if len(new_name) > max_chars:
        new_name = new_name[:max_chars]  # get at most 64 chars
        if new_name.rfind(blank) > 0:
            new_name = new_name[:new_name.rfind(blank)]  # nearest word
    return new_name


def prettify(name, blank=" "):
    """
    :param name: string
        Name to edit
    :param blank: string
        Default blanks in name.
    :return: string
        Prettier name from given one: replace bad chars with good ones.
    """

    if name.startswith("."):  # remove starting .
        name = name[1:]

    for bad_char in BAD_CHARS:
        name = name.replace(bad_char, blank)  # remove token

    name = name.replace(" ", blank)  # replace blanks
    while name.find(blank + blank) >= 0:  # while there are blanks
        name = name.replace(blank + blank, blank)

    for i in range(1, len(name) - 2):
        try:
            if name[i - 1] == blank and \
                            name[i + 1] == blank and \
                            name[i] in BAD_CHARS:
                name = name[:i - 1] + name[i + 2:]
        except Exception:  # out of bounds
            pass

    if name.startswith(blank):
        name = name[1:]

    if name.endswith(blank):  # remove ending replacement
        name = name[:-1]

    return name


def is_file(path):
    """
    :param path: str
        Path to check
    :return: bool
        True iff path is a file
    """

    return os.path.isfile(path)


def is_folder(path):
    """
    :param path: str
        Path to check
    :return: bool
        True iff path is a file
    """

    return os.path.isdir(path)


def get_parent_folder(file_path):
    """
    :param file_path: str
        Path to file or folder
    :return: str
        Name of folder container
    """

    return os.path.split(os.path.split(os.path.abspath(file_path))[0])[-1]


def ls_dir(path, include_hidden=False):
    """
    :param path: string
        Path to directory to get list of files and folders
    :param include_hidden: bool
        Whether to include hidden files in list.
    :return: list
        List of paths in given directory.
    """

    lst = []
    for file in os.listdir(path):
        hidden_file = FileSystem(file).is_hidden()
        if (hidden_file and include_hidden) or (not hidden_file):
            lst.append(os.path.join(path, file))
    return lst


def ls_recurse(path, include_hidden=False):
    """
    :param path: string
        Path to directory to get list of files and folders
    :param include_hidden: bool
        Whether to include hidden files in list.
    :return: list
        List of paths in given directory recursively.
    """

    lst = []
    for file in os.listdir(path):
        hidden_file = FileSystem(file).is_hidden()
        if (hidden_file and include_hidden) or (not hidden_file):
            lst.append(os.path.join(path, file))
            if os.path.isdir(os.path.join(path, file)):
                lst += ls_recurse(
                    os.path.join(path, file),
                    include_hidden=include_hidden
                )  # get list of files in directory
    return lst


def list_content(path, recurse, include_hidden=False):
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
        return ls_recurse(path, include_hidden=include_hidden)

    return ls_dir(path, include_hidden=include_hidden)


class FileSystem(object):
    """ Models a folder/file in a OS """

    def __init__(self, path):
        """
        :param path: string
            Path to file
        """

        object.__init__(self)

        self.path = fix_raw_path(path)
        self.name, self.extension = os.path.splitext(self.path)

    def is_hidden(self):
        """
        :return: bool
            True iff path is hidden
        """

        return self.name.startswith(".")

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
        for char in RUSSIAN_CHARS:
            if char in self.name:
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

        rename_path = fix_raw_path(new_path)
        if os.path.isdir(self.path):
            os.rename(self.path, rename_path)
        else:
            os.renames(self.path, rename_path)
