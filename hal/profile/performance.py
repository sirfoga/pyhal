# -*- coding: utf-8 -*-

"""Perform benchmarks and tests on your PC """

import getpass
import os
import random
import sys
from time import time

from hal.files.models.files import Document
from hal.maths.problems import EightQueen

# todo use logging


INTRO = "So, let\'s get into the details.. I\'m going to solve the " \
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


class EightQueenTest:
    """Test CPU by solving eight-queen problem"""

    def __init__(self, size):
        """
        :param size: size of test
        """
        self.size = size
        self.benchmark = ""

    @staticmethod
    def welcome():
        """Welcomes user to this test sessions

        :returns: intro to test
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
        """Welcomes user to this test sessions

        :returns: intro to test
        """
        return INTRO

    def run_test(self):
        """Runs test

        :returns: Time to solve problem with given size
        """
        timing = time()
        problem = EightQueen(self.size)
        problem.solve(problem.board_size)
        return time() - timing

    def update_std_out_and_log(self, string):
        """Prints to stdout and updates log

        :param string: Stuff to print
        """
        print(string)  # update stdout
        self.benchmark += "\n" + string  # update log

    def start(self):
        """Starts profiling"""
        self.update_std_out_and_log(self.welcome())
        print(EightQueenTest.introduction())

        if input("Are you sure you want to proceed? [y/n]").startswith("y"):
            self.run()
        else:
            print("Bye bye!")
            sys.exit(0)

    def run(self):
        """Runs test and safes results"""
        max_board_size = self.size
        start_time = time()

        for size in range(max_board_size + 1):
            timing = self.run_test()
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
            file_name = "EightQueenTest" + str(int(random.random() * 10000)) \
                        + ".log"
            log_file = os.path.join(os.getcwd(), file_name)
            Document.write_data_to_file(self.benchmark, log_file)

            print("The log file is", log_file)
