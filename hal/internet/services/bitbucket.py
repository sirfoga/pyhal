# -*- coding: utf-8 -*-

""" Common classes and entities in Bitbucket """

BITBUCKET_REMOTE = "https://{}@bitbucket.org/"


def get_clone_url(remote_shortcut, user):
    """

    :param remote_shortcut: str
    :param Remote: relative path of repository to clone
    :param user: str
    :param User: to clone with
    :returns: str
      Url to clone
    """
    return BITBUCKET_REMOTE.format(user) + remote_shortcut
