# -*- coding: utf-8 -*-

""" Cron-ify python apps with simple config files """

import datetime
import json


class AppCronLock:
    """Checks if app can proceed; generates lock"""

    DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"

    def __init__(self, lock_file):
        """
        :param lock_file: str
            Path to lock file
        """
        self.lock_file = lock_file
        self.update_interval = 7
        self.last_update = datetime.datetime.fromtimestamp(0)
        self.data = None
        self.parse_lock()

    def set_update_interval(self, days=7):
        """
        # Arguments
          days: int
        Days between 2 consecutive app updates (Default value = 7)

        # Returns:
          void
          Sets app interval update

        """
        self.update_interval = days

    def can_proceed(self):
        """:return: bool
            True iff app is not locked and times since last update < app
            update interval

        # Arguments

        # Returns:

        """
        now = datetime.datetime.now()
        return now >= self.last_update + \
                      datetime.timedelta(days=self.update_interval)

    def parse_lock(self):
        """:return: {}
            Details about last update

        # Arguments

        # Returns:

        """
        try:
            with open(self.lock_file, "r") as reader:
                data = json.loads(reader.read())
                self.last_update = datetime.datetime.strptime(
                    data["last_update"],
                    AppCronLock.DATETIME_FORMAT
                )
        except:  # malformed lock file
            self.write_lock(last_update=datetime.datetime.fromtimestamp(0))
            self.parse_lock()

    def write_lock(self, last_update=datetime.datetime.now()):
        """:return: void
            Writes lock file

        # Arguments
          last_update:  (Default value = datetime.datetime.now())

        # Returns:

        """
        data = {
            "last_update": last_update.strftime(AppCronLock.DATETIME_FORMAT)
        }

        with open(self.lock_file, "w") as writer:
            json.dump(data, writer)
