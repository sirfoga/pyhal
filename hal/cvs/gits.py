#!/usr/bin/env python
# coding: utf-8


"""Handles main models in git repository"""

from git import Repo
from unidiff import PatchSet

from hal.cvs.versioning import Version


class Diff:
    """Git diff result"""

    ADD = "added"
    DEL = "removed"

    def __init__(self, diff):
        """
        :param diff: Diff between 2 commits
        """
        self.diff = diff

    def __str__(self):
        totals = self.get_totals()
        return "+", totals[self.ADD], " -", totals[self.DEL]

    def get_totals(self):
        """Calculates total additions and deletions

        :return: Dictionary with totals
        """
        total_added = 0
        total_removed = 0

        patch = PatchSet(self.diff)
        total_added += sum([
            edit.added for edit in patch
        ])
        total_removed += sum([
            edit.removed for edit in patch
        ])

        return {
            self.ADD: total_added,
            self.DEL: total_removed
        }


class Commit:
    """Git repository commit"""

    def __init__(self, commit):
        """

        :param commit: Commit of repository
        """
        self.commit = commit

    def __str__(self, date_format="%H:%M:%S %y-%m-%d %z"):
        """
        Converts to string

        :param date_format: Format date and times with this format
        :return: Pretty description of commit
        """
        hash_value = self.commit.hexsha
        date_time = self.commit.authored_datetime.strftime(date_format)
        return hash_value + " at " + date_time

    def get_author(self):
        """Gets author

        :return: author of commit
        """
        author = self.commit.author

        out = ""
        if author.name is not None:
            out += author.name

        if author.email is not None:
            out += " (" + author.email + ")"

        return out


class Repository:
    """Git repository"""

    def __init__(self, repo_path):
        """

        :param repo_path: Path to repository
        """
        self.repo = Repo(repo_path)

    def get_last_commit(self):
        """Gets last commit

        :return: Last commit of repository
        """
        return self.repo.head.commit

    def get_diff_amounts(self):
        """Gets list of total diff

        :return: List of total diff between 2 consecutive commits since start
        """
        diffs = []

        last_commit = None
        for commit in self.repo.iter_commits():
            if last_commit is not None:
                diff = self.get_diff(commit.hexsha, last_commit.hexsha)
                total_changed = diff[Diff.ADD] + diff[Diff.DEL]
                diffs.append(total_changed)

            last_commit = commit

        return diffs

    def get_diff(self, commit, other_commit):
        """Calculates total additions and deletions

        :param commit: First commit
        :param other_commit: Second commit
        :return: dictionary: Dictionary with total additions and deletions
        """
        print(other_commit, "VS", commit)
        diff = self.repo.git.diff(commit, other_commit)
        return Diff(diff).get_totals()

    def get_version(self, diff_to_increase_ratio):
        """Gets version

        :param diff_to_increase_ratio: Ratio to convert number of changes into
        :return: Version of this code, based on commits diffs
        """
        diffs = self.get_diff_amounts()
        version = Version()

        for diff in diffs:
            version.increase_by_changes(diff, diff_to_increase_ratio)

        return version

    def get_new_version(self, last_version, last_commit,
                        diff_to_increase_ratio):
        """Gets new version

        :param last_version: last version known
        :param last_commit: hash of commit of last version
        :param diff_to_increase_ratio: Ratio to convert number of changes into
        :return: new version
        """

        version = Version(last_version)
        diff = self.get_diff(last_commit, self.get_last_commit_hash())
        total_changed = diff[Diff.ADD] + diff[Diff.DEL]

        version.increase_by_changes(total_changed, diff_to_increase_ratio)
        return version

    def get_pretty_version(self, diff_to_increase_ratio):
        """Pretty version

        :param diff_to_increase_ratio: Ratio to convert number of changes into
            version increases
        :return: string: Pretty version of this repository
        """
        version = self.get_version(diff_to_increase_ratio)
        build = self.get_last_commit_hash()
        return str(version) + " (" + build + ")"

    def get_last_commit_hash(self):
        """Gets hash of last commit

        :return: hash of last commit
        """
        last = self.get_last_commit()
        return str(last.hexsha)
