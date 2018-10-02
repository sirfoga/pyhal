# !/usr/bin/python3
# coding: utf-8


""" Perform benchmarks and tests on your PC """

import getpass
import os
import random
import sys

from hal.files.models import Document
from hal.maths import maths
from times import time


class EightQueenTest(object):
    """ Test CPU by solving eight-queen problem """

    def __init__(self, size):
        object.__init__(self)

        self.size = size
        self.benchmark = ""

    @staticmethod
    def welcome():
        """
        :return: string
            Welcomes user to this test sessions
        """

        user = getpass.getuser()
        os_name = os.name

        output = "\nHello! You are " + str(user) + " running " + str(
            os_name) + " right?\n"
        output += "I\'ll test your CPU and RAM usage while executing this " \
                  "script, is it ok?\n "
        return output

    @staticmethod
    def introduction():
        """ :return: string
            Welcomes user to this test sessions
        """

        output = "So, let\'s get into the details.. I\'m going to solve the " \
                 "classic Eight Queens Puzzle: it\'s the problem of placing " \
                 "eight chess queens on an 8×8 chessboard so that no two " \
                 "queens threaten each other.\nFinding all solutions to the " \
                 "eight queens puzzle is a good example of a nontrivial " \
                 "problem. For this reason, it is often used as an example " \
                 "problem for various programming techniques, including " \
                 "non-traditional approaches such as constraint programming," \
                 " logic programming or genetic algorithms. Most often, " \
                 "it is used as an example of a problem that can be solved " \
                 "with a recursive algorithm (read more here: " \
                 "https://en.wikipedia.org/wiki/Eight_queens_puzzle) ... and" \
                 " since recursion involves both RAM storage and CPU use of " \
                 "your machine, this problem is a good tester to test your " \
                 "PC speed! Now let\'s get started.. "
        return output

    @staticmethod
    def run_test_with_size(size):
        """
        :param size: int
            Number of rows in grid
        :return: int
            Time to solve problem with given size
        """

        timing = time()
        problem = maths.EightQueen(size)
        problem.solve(problem.board_size)
        return time() - timing

    def update_std_out_and_log(self, string):
        """
        :param string: string
            Stuff to print
        :return: void
            Prints to stdout and updates log
        """

        print(string)  # update stdout
        self.benchmark += "\n" + string  # update log

    def start(self):
        """
        :return: void
            Starts profiling
        """

        self.update_std_out_and_log(self.welcome())
        print(EightQueenTest.introduction())

        if input("Are you sure you want to proceed? [y/n]").startswith("y"):
            self._run()
        else:
            print("Bye bye!")
            sys.exit(0)

    def _run(self):
        max_board_size = self.size
        start_time = time()

        for size in range(max_board_size + 1):
            timing = self.run_test_with_size(size)
            self.update_std_out_and_log(
                "BOARD SIZE".ljust(10) +
                str(size).ljust(10) + "TIME REQUIRED (s)".ljust(20) +
                str('{:03.3f}'.format(timing))
            )

        finish_time = time()
        length = finish_time - start_time

        self.update_std_out_and_log(
            "It took me " + str(length) + " seconds to complete all " + str(
                max_board_size) + " problems.\nThanks for your patience!")
        if input("Do you wanna save the results? [y/n]").startswith("y"):
            conf_file = os.path.join(os.getcwd(), "EightQueenTest" + str(
                int(random.random() * 10000)) + ".conf")
            Document.write_data_to_file(self.benchmark, conf_file)

            print(
                "Just one extra moment of patience .. I\'ll save a "
                "configuration file..\n "
                "Done! The configuration file is \'" + conf_file + "\'")
