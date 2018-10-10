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
        self.d = diff

    def __str__(self):
        totals = self.get_totals()
        return "+", totals[self.ADD], " -", totals[self.DEL]

    def get_totals(self):
        """Calculates total additions and deletions
        
        :returns: Dictionary with totals
        """
        total_added = 0
        total_removed = 0

        patch = PatchSet(self.d)
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
        self.c = commit

    def __str__(self, date_format="%H:%M:%S %y-%m-%d %z"):
        """
        Converts to string

        :param date_format: Format date and times with this format
        :returns: Pretty description of commit
        """
        hash_value = self.c.hexsha
        date_time = self.c.authored_datetime.strftime(date_format)
        return hash_value + " at " + date_time

    def get_author(self):
        """Gets author
        
        :returns: author of commit
        """
        author = self.c.author

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
        self.r = Repo(repo_path)

    def get_last_commit(self):
        """Gets last commit
        
        :returns: Last commit of repository
        """
        return self.r.head.commit

    def get_diff_amounts(self):
        """Gets list of total diff
        
        :returns: List of total diff between 2 consecutive commits since start
        """
        diffs = []

        last_commit = None
        for commit in self.r.iter_commits():
            if last_commit is not None:
                diff = self.get_diff(commit, last_commit)
                total_changed = diff[Diff.ADD] + diff[Diff.DEL]
                diffs.append(total_changed)

            last_commit = commit

        return diffs

    def get_diff(self, commit, other_commit):
        """Calculates total additions and deletions

        :param commit: First commit
        :param other_commit: Second commit
        :returns: dictionary: Dictionary with total additions and deletions
        """
        diff = self.r.git.diff(commit.hexsha, other_commit.hexsha)
        return Diff(diff).get_totals()

    def get_version(self, diff_to_increase_ratio):
        """Gets version

        :param diff_to_increase_ratio: Ratio to convert number of changes into
        :returns: Version of this code, based on commits diffs
        """
        diffs = self.get_diff_amounts()
        version = Version()

        for diff in diffs:
            version.increase_by_changes(diff, diff_to_increase_ratio)

        return version

    def get_pretty_version(self, diff_to_increase_ratio):
        """Pretty version

        :param diff_to_increase_ratio: Ratio to convert number of changes into
            version increases
        :returns: string: Pretty version of this repository
        """
        version = self.get_version(diff_to_increase_ratio)
        build = self.get_last_commit_hash()
        return str(version) + " (" + build + ")"

    def get_last_commit_hash(self):
        """Gets hash of last commit

        :returns: hash of last commit
        """
        last = self.get_last_commit()
        return str(last.hexsha)
