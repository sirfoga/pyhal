# !/usr/bin/python3
# coding: utf-8


""" Songs in various formats """

from mutagen.id3 import ID3
from mutagen.id3._frames import TIT2, TPE1, TALB, TRCK, TDRC, TCON
from mutagen.mp3 import MP3

from hal.files.models.system import FileSystem
from hal.files.models.system import list_content


def find_songs(folder, recursive):
    """
    Args:
      folder: str
    Path
      recursive: bool
    True iff want to search recursively

    Returns:
      generator of MP3Song
      List of paths of the songs in folder
    """
    paths = list_content(folder, recursive)
    for p in paths:
        if MP3Song.is_valid_mp3(p):
            yield MP3Song(p)


class MP3Song(FileSystem):
    """mp3 song"""

    @staticmethod
    def is_valid_mp3(path):
        """
        Args:
          path: str
        Path to candidate .mp3 song

        Returns:
          bool
          True iff song is MP3 encoded

        """
        try:
            MP3(path)
            return True
        except Exception as e:
            return False

    def __init__(self, path):
        """
        :param path: str
            Location of .mp3 file
        """
        super().__init__(path)

        self.song = MP3(self.path, ID3=ID3)
        self.tags = self.song.tags

    def get_details(self):
        """:return: {}
            Dictionary with songs details about title, artist, album and year

        Args:

        Returns:

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

    # setters

    def set_title(self, name):
        """
        Args:
          name: str
        Song's title

        Returns:
          void
          Sets song's title

        """
        self.tags.add(TIT2(encoding=3, text=name.decode('utf-8')))
        self.song.save()

    def set_artist(self, artist):
        """
        Args:
          artist: str
        Song's artist

        Returns:
          void
          Sets song's artist

        """
        self.tags.add(TPE1(encoding=3, text=artist.decode('utf-8')))
        self.song.save()

    def set_album(self, album):
        """
        Args:
          album: str
        Song's album

        Returns:
          void
          Sets song's albu

        """
        self.tags.add(TALB(encoding=3, text=album.decode('utf-8')))
        self.song.save()

    def set_nr_track(self, nr_track):
        """
        Args:
          nr_track: int
        Number of track

        Returns:
          void
          Sets song's track number

        """
        self.tags.add(TRCK(encoding=3, text=str(nr_track)))
        self.song.save()

    def set_year(self, year):
        """
        Args:
          year: int
        Year of song

        Returns:
          void
          Sets song's year

        """
        self.tags.add(TDRC(encoding=3, text=str(year)))
        self.song.save()

    def set_genre(self, genre):
        """
        Args:
          genre: str
        Genre of song

        Returns:
          void
          Sets song's genre

        """
        self.tags.add(TCON(encoding=3, text=str(genre)))
        self.song.save()

    # getters

    def get_title(self):
        """:return: str
            Gets song's title

        Args:

        Returns:

        """
        try:
            return self.tags.get("TIT2").text[0]
        except Exception:
            return None

    def get_artist(self):
        """:return: str
            Gets song's artist

        Args:

        Returns:

        """
        try:
            return self.tags.get("TPE1").text[0]
        except Exception:
            return None

    def get_album(self):
        """:return: str
            Gets song's albu

        Args:

        Returns:

        """
        try:
            return self.tags.get("TALB").text[0]
        except Exception:
            return None

    def get_nr_track(self):
        """:return: str
            Gets song's track number

        Args:

        Returns:

        """
        try:
            return self.tags.get("TRCK").text[0]
        except Exception:
            return None

    def get_year(self):
        """:return: str
            Gets song's year

        Args:

        Returns:

        """
        try:
            return self.tags.get("TDRC").text[0]
        except Exception:
            return None

    def get_genre(self):
        """:return: str
            Gets song's genre

        Args:

        Returns:

        """
        try:
            return self.tags.get("TCON").text[0]
        except Exception:
            return None
