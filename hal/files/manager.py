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


""" Popular actions one may do to files and folders. """


import os
import re


BAD_CHARS = [
    ".", ":", "\"", "’", "&", "720p", "1080p", "yify", ",", "\"S", "brrip", "bluray", "Bokutox", "x264", "[", "]", "sparks", "h264",
    "aac", "ozlem", "ac3", "ozlem", "etrg", "dvdrip", "xvid", "nydic", "sujaidr", "x265", "hevc", "(pimprg)", "aac",
    "ozlem", "remastered", "anoxmous", "yts"]
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


def is_video(f):
    """
    :param f: string
        Document name.
    :return: True iff document is a video.
    """

    filename, file_extension = os.path.splitext(f)
    return file_extension.lower() in VIDEO_FORMAT


def is_subtitle(f):
    """
    :param f: string
        Document name.
    :return: True iff document is a subtitle.
    """

    filename, file_extension = os.path.splitext(f)
    return file_extension.lower() in SUBTITLE_FORMAT


def is_text(f):
    """
    :param f: string
        Document name.
    :return: True iff document is a text file.
    """

    filename, file_extension = os.path.splitext(f)
    return file_extension.lower() in TEXT_FORMAT


def is_image(f):
    """
    :param f: string
        Document name.
    :return: True iff document is an image.
    """

    filename, file_extension = os.path.splitext(f)
    return file_extension.lower() in IMAGE_FORMAT


def is_audio(f):
    """
    :param f: string
        Document name.
    :return: True iff document is an audio.
    """

    filename, file_extension = os.path.splitext(f)
    return file_extension.lower() in AUDIO_FORMAT


def is_archive_mac(d):
    """
    :param f: string
        Document name.
    :return: True iff document is an MACOSX archive.
    """

    return "macosx" in d.lower()


def is_russian(f):
    """
    :param f: string
        Document name.
    :return: True iff document has a russian name.
    """

    filename, file_extension = os.path.splitext(f)
    russian_chars = 0
    for c in RUSSIAN_CHARS:
        if c in filename:
            russian_chars += 1  # found a russian char
    return russian_chars > len(RUSSIAN_CHARS) / 2.0


def is_hidden(path_name):
    """
    :param path_name: string
        File name or directory name to check if hidden
    :return: bool
        True iff path is hidden
    """

    return path_name.startswith(".")


def prettify(s, r=" "):
    """
    :param s: string
        Name of file of folder.
    :param r: string
        Default blanks in name.
    :return: string
        Prettier name from given one: replace bad chars with good ones.
    """

    if s.startswith("."):  # remove starting .
        name = s[1:]
    else:
        name = s

    for t in BAD_CHARS:
        name = name.replace(t.lower(), r)  # remove token
    name = name.replace(" ", r)  # replace blanks
    for _ in range(10):  # remove following blanks
        name = name.replace(r + r, r)

    for i in range(1, len(name) - 2):  # loop through characters except 1 and end
        try:
            if name[i - 1] == r and name[i + 1] == r:  # 2 replacement hug one good char
                name = name[:i - 1] + name[i + 1:]
        except:  # out of bounds
            pass

    if name.endswith(r):  # remove ending replacement
        name = name[:-1]

    return name


def remove_year(s):
    """
    :param s: string
        Name of document.
    :return: string
        Given string bu with no years.
    """

    name = s
    l_bracket, r_bracket = name.find("("), name.find(")")  # find limits of year
    if r_bracket - l_bracket + 1 == 6:  # there is a year in between
        name = name.replace(name[l_bracket: r_bracket + 1], "")  # remove year
    else:
        l_bracket, r_bracket = name.find("["), name.find("]")  # try with square brackets
        if r_bracket - l_bracket + 1 == 6:  # there is a year in between
            name = name.replace(name[l_bracket: r_bracket + 1], "")  # remove year

    for i in range(len(name) - 4):
        try:
            if name[i: i + 4].isdigit():
                name = name[:i] + name[i + 4:]
        except:
            pass

    return name


def remove_brackets(s):
    """
    :param s: string
        Name of document.
    :return: string
        Given string bu with no barckets.
    """

    name = re.sub("([\(\[]).*?([\)\]])", "\g<1>\g<2>", s)
    name = name.replace("()", "")  # remove anything in ()
    if name.rfind("(") > 0:  # there exists a "("
        name = name[:name.rfind("(")]
    name = name.replace("(", "")
    name = name.replace(")", "")
    for _ in range(10):
        name = name.replace("  ", " ")  # remove extra blanks
    name = name.strip()
    return name


def extract_path_name(path):
    """
    :param path: string
        Path to document to extract name
    :return: tuple string, string
        Name of path, name of file (or folder)
    """

    if os.path.isdir(path):
        p = os.path.dirname(os.path.abspath(path))
        name = path.replace(p + os.path.sep, "")[: -1]  # replace in full path, dir path to get name
    else:
        p, name = os.path.dirname(os.path.abspath(path)), os.path.basename(path)
    return p, name


def extract_name_max_chars(name, max_chars, blank=" "):
    """
    :param name: string
        Name to edit.
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
