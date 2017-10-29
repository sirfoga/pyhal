# !/usr/bin/python3
# coding: utf-8

# Copyright 2016-2018 Stefano Fogarollo
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


""" Deal with user on standard output/input """

from hal.strings.utils import get_max_similar


class UserInput(object):
    """ Chat with user and ask questions """

    YES = ["yes", "ok", "fine"]
    NO = ["no", "not ok", "none"]
    THRESHOLD_INPUT = 0.9

    def __init__(self, yes_choices=YES, no_choices=NO,
                 threshold=THRESHOLD_INPUT, interactive=True):
        """
        :param threshold: float [0, 1]
            Match user answer with the one provided with at least this rate
        :param yes_choices: [] of str
            List of answer considered a "yes"
        :param no_choices: [] of str
            List of answer considered a "no"
        :param interactive: bool
            True iff program should deal with user not answering properly
        """

        object.__init__(self)

        self.THRESHOLD_INPUT = threshold
        self.YES = yes_choices
        self.NO = no_choices
        self.last_question = None
        self.interactive = bool(interactive)

    def is_yes(self, answer):
        """
        :param answer: str
            User answer
        :return: bool
            True iff considered a "yes" answer
        """

        yes_sim, = get_max_similar(answer, self.YES)
        no_sim, = get_max_similar(answer, self.NO)
        return yes_sim > no_sim and yes_sim > self.THRESHOLD_INPUT

    def is_no(self, answer):
        """
        :param answer: str
            User answer
        :return: bool
            True iff considered a "yes" answer
        """

        yes_sim, = get_max_similar(answer, self.YES)
        no_sim, = get_max_similar(answer, self.NO)
        return no_sim > yes_sim and no_sim > self.THRESHOLD_INPUT

    def show_help(self):
        """
        :return: void
            Prints to stdout help on how to answer properly
        """

        print("Sorry, not well understood.")
        print("- use", str(self.YES), "to answer 'YES'")
        print("- use", str(self.NO), "to answer 'NO'")

    def re_ask(self, with_help=True):
        """
        :param with_help: bool
            True iff you want to show help on how to answer questions
        :return: void
            Re-asks user the last question
        """

        if with_help:
            self.show_help()

        return self.get_raw_answer(self.last_question)

    def get_raw_answer(self, question):
        """
        :param question: str
            Question to ask user
        :return: str
            User answer
        """

        self.last_question = str(question).strip()
        user_answer = input(self.last_question)
        return user_answer.strip()

    def get_yn_answer(self, question):
        """
        :param question: str
            Question to ask user
        :return: bool
            User answer
        """

        user_answer = self.get_raw_answer(question).lower()
        if user_answer in self.YES:
            return True

        if user_answer in self.NO:
            return False

        is_yes = self.is_yes(user_answer)  # check if similar to yes/no choices
        is_no = self.is_no(user_answer)
        if is_yes and not is_no:
            return True

        if is_no and not is_yes:
            return False

        if self.interactive:
            self.show_help()
            self.get_yn_answer(self.last_question)
        else:
            return False

    def get_int_answer(self, question):
        """
        :param question: str
            Question to ask
        :return: int
            User answer
        """

        try:
            user_answer = self.get_raw_answer(question)
            return int(user_answer)
        except Exception as e:
            print("Int not properly formatted")
            print(str(e))
            self.get_int_answer(self.last_question)
