#!/usr/bin/env python
# coding: utf-8


""" Gets pretty version of repository """

from git import Repo


class Versionifier:
    """ Pretty version manager for git repositories """

    def __init__(self, repo_path):
        """
        :param repo_path: str
            Path to repository
        """

        self.r = Repo(repo_path)

    @staticmethod
    def pretty_commit(commit, date_format="%H:%M:%S %y-%m-%d %z"):
        """
        :param commit: git.Commit
            Commit
        """
