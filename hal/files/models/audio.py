# -*- coding: utf-8 -*-

"""Songs in various formats """

from mutagen.id3 import ID3
from mutagen.id3._frames import TIT2, TPE1, TALB, TRCK, TDRC, TCON
from mutagen.mp3 import MP3

from hal.files.models.system import FileSystem
from hal.files.models.system import list_content
from hal.wrappers.errors import true_false_returns, none_returns


def find_songs(folder, recursive):
    """

    :param folder: folder path
    :param recursive: True  want to search recursively
    :returns: generator of) paths of the songs in folder

    """
    paths = list_content(folder, recursive)
    for p in paths:
        if MP3Song.is_valid_mp3(p):
            yield MP3Song(p)


class MP3Song(FileSystem):
    """.mp3 song"""

    @staticmethod
    def is_valid_mp3(path):
        """

        :param path: candidate
        :returns: True iff song is MP3 encoded
        """
        try:
            MP3(path)
            return True
        except:
            return False

    def __init__(self, path):
        """
        :param path: Location of .mp3 file
        """
        super().__init__(path)
        self.song = MP3(self.path, ID3=ID3)
        self.tags = self.song.tags

    def get_details(self):
        """Finds songs details

        :returns: Dictionary with songs details about title, artist, album and year
        """
        title = str(self.get_title()).strip()
        artist = str(self.get_artist()).strip()
        album = str(self.get_album()).strip()
        year = str(self.get_year()).strip()

        return {
            "title": title,
            "artist": artist,
            "album": album,
            "year": year
        }

    @true_false_returns
    def _set_attr(self, attribute):
        """Sets attribute of song

        :param attribute: Attribute to save
        :returns: True iff operation completed
        """

        self.tags.add(attribute)
        self.song.save()

    def set_title(self, name):
        """Sets song's title

        :param name: title
        """
        self._set_attr(TIT2(encoding=3, text=name.decode('utf-8')))

    def set_artist(self, artist):
        """Sets song's artist

        :param artist: artist
        """
        self._set_attr(TPE1(encoding=3, text=artist.decode('utf-8')))

    def set_album(self, album):
        """Sets song's album

        :param album: album
        """
        self._set_attr(TALB(encoding=3, text=album.decode('utf-8')))

    def set_nr_track(self, nr_track):
        """Sets song's track numb

        :param nr_track: of track
        """
        self._set_attr(TRCK(encoding=3, text=str(nr_track)))

    def set_year(self, year):
        """Sets song's year

        :param year: year
        """
        self._set_attr(TDRC(encoding=3, text=str(year)))

    def set_genre(self, genre):
        """Sets song's genre

        :param genre: genre
        """
        self._set_attr(TCON(encoding=3, text=str(genre)))

    @none_returns
    def _get_attr(self, key):
        """Gets attribute of song

        :param key: Name of attribute to get
        :returns: Attribute
        """
        return self.tags.get(key).text[0]

    def get_title(self):
        """Gets song's title

        :returns: title
        """
        return self._get_attr("TIT2")

    def get_artist(self):
        """Gets song's artist

        :returns: artist
        """
        return self._get_attr("TPE1")

    def get_album(self):
        """Gets song's albu

        :returns: album
        """
        return self._get_attr("TALB")

    def get_nr_track(self):
        """Gets song's track number

        :returns: # of track
        """
        return self._get_attr("TRCK")

    def get_year(self):
        """Gets song's year

        :returns: year
        """
        return self._get_attr("TDRC")

    def get_genre(self):
        """Gets song's genre

        :returns: genre
        """
        return self._get_attr("TCON")
