# -*- coding: utf-8 -*-

"""Common classes and entities in Bitbucket """

BITBUCKET_REMOTE = "https://{}@bitbucket.org/"


def get_clone_url(remote_shortcut, user):
    """Finds clone url of repository

    :param remote_shortcut: relative path of repository to clone
    :param user: User to clone with
    :returns: Url to clone

    """
    return BITBUCKET_REMOTE.format(user) + remote_shortcut
