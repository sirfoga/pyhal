# !/usr/bin/python3
# coding: utf-8


""" Common classes and entities in Bitbucket """

BITBUCKET_REMOTE = "https://{}@bitbucket.org/"


def get_clone_url(remote_shortcut, user):
    """
    # Arguments
      remote_shortcut: str
    Remote relative path of repository to clone
      user: str
    User to clone with

    # Returns:
      str
      Url to clone
    """
    return BITBUCKET_REMOTE.format(user) + remote_shortcut
