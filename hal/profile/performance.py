# !/usr/bin/python
# coding: utf_8

# Copyright 2016 Stefano Fogarollo
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


""" Perform benchmarks and tests on your PC. """

import getpass
import os
import sys
import time

from hal import maths
from hal.files.models import Document


class EightQueenTest(object):
    """ test CPU by solving eight-queen problem """

    def __init__(self, size):
        object.__init__(self)
        self.size = size

    @staticmethod
    def welcome():
        """ :return: introduce script """

        output = ""
        output += "\nHello! You are.."
        user = getpass.getuser()
        output += "\nUsername".ljust(20) + str(user.username)
        output += "\nOS".ljust(20) + str(user.os)
        output += "\nThis directory".ljust(20) + str(user.work_dir)
        output += "\n..I am TEST: I\"ll test your CPU and RAM usage while executing this script"
        return output

    @staticmethod
    def introduction():
        """ :return: introduce 8 queen problem """

        output = "So, let\"s get into the details.." \
              "The eight queens puzzle is the problem of placing eight chess queens on an 8×8 chessboard so that no two queens threaten each other." \
              "Thus, a solution requires that no two queens share the same row, column, or diagonal\n" \
              "...\n" \
              "Finding all solutions to the eight queens puzzle is a good example of a simple but nontrivial problem." \
              "For this reason, it is often used as an example problem for various programming techniques, including nontraditional approaches such as constraint programming, logic programming or genetic algorithms." \
              "Most often, it is used as an example of a problem that can be solved with a recursive algorithm ..\n" \
              "read more here: https://en.wikipedia.org/wiki/Eight_queens_puzzle\n" \
              ".. and since recursion involves both RAM storage and CPU use of your machine, this problem is a good tester to test your PC speed!" \
              "Now let\"s get started.."
        return output

    def run(self):
        benchmark = ""
        print(EightQueenTest.welcome())
        benchmark += EightQueenTest.welcome()
        print(EightQueenTest.introduction())
        benchmark += "\n" + EightQueenTest.introduction()

        if input("Are you sure you want to proceed? [y/n]").startswith("y"):
            max_board = self.size
            start_time = time.time()
            for size in range(max_board + 1):
                timing = time.time()
                problem = maths.EightQueen(size)
                problem.solve(problem.board_size)
                timing = time.time() - timing
                print("BOARD SIZE".ljust(20) + str(size).ljust(20) + "TIME REQUIRED (s)".ljust(20) + str(timing))
                benchmark += "\nBOARD SIZE".ljust(20) + str(size).ljust(20) + "TIME REQUIRED (s)".ljust(20) + str(timing)
            finish_time = time.time()
            length = finish_time - start_time
            print("It took me " + str(length) + " seconds to complete all " + str(max_board) + " problems.\nThanks for your patience!")
            benchmark += "\nIt took me " + str(length) + " seconds to complete all " + str(max_board) + " problems.\nThanks for your patience!"
            conf_file = os.path.join(os.getcwd(), str(id(benchmark)))
            Document.write_data_to_file(benchmark, conf_file)
            print("Just one extra moment of patience .. I\"ll save a configuration file..\n"
                  "Done! The configuration file is \"" + conf_file + ".conf" + "\"")
        else:
            print("Now exiting!")
            sys.exit(0)
