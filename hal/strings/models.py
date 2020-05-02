# -*- coding: utf-8 -*-

"""String models"""

import unicodedata

from pyparsing import Literal, Word, nums, Combine, Optional, delimitedList, \
    alphas, oneOf, Suppress


class String:
    """Models string"""

    def __init__(self, string):
        self.string = str(string)

    def remove_escapes(self):
        """Removes everything except number and letters from string

        :return: All numbers and letters in string
        """
        chars = []

        i = 0
        while i < len(self.string):
            char = self.string[i]
            if char == "\\":
                i += 1
            else:
                chars.append(char)

            i += 1

        return "".join(chars)

    def remove_non_ascii(self):
        """Removes non-ansi chars from text

        :return: input except non-ansi chars
        """
        return ''.join(c for c in self.string if ord(c) < 128)

    def convert_accents(self):
        """Removes accents from text

        :return: input with converted accents chars
        """
        nkfd_form = unicodedata.normalize('NFKD', self.string)
        return "".join([
            char
            for char in nkfd_form
            if not unicodedata.combining(char)
        ])

    def remove_control_chars(self):
        """Removes controls chars from text
    
        :return: input except controls chars
        """
        esc_key = Literal('\x1b')
        integer = Word(nums)
        escape_seq = Combine(
            esc_key + '[' + Optional(delimitedList(integer, ';')) +
            oneOf(list(alphas)))

        return Suppress(escape_seq).transformString(self.string)

    def is_well_formatted(self):
        """Checks if string is good formatted
    
        :return: True iff string is good formatted
        """
        # False iff there are at least \n, \r, \t,"  "
        is_bad_formatted = ":" in self.string or \
                           "\\'" in self.string or \
                           "\n" in self.string or \
                           "\r" in self.string or \
                           "\t" in self.string or \
                           "\\n" in self.string or \
                           "\\r" in self.string or \
                           "\\t" in self.string or \
                           "  " in self.string
        return not is_bad_formatted

    def strip_bad_html(self):
        """Strips string of all HTML elements
    
        :return: Given string with raw HTML elements removed
        """
        out = self.string
        while not String(out).is_well_formatted():
            out = out.replace(":", "") \
                .replace("\\'", "\'") \
                .replace("\\n", "") \
                .replace("\\r", "") \
                .replace("\\t", "") \
                .replace("\n", "") \
                .replace("\r", "") \
                .replace("\t", "") \
                .replace("  ", " ") \
                .strip()

        return str(out)

    def remove_all(self, token):
        """Removes all occurrences of token

        :param token: string to remove
        :return: input without token
        """

        out = self.string.replace(" ", token)  # replace tokens
        while out.find(token + token) >= 0:  # while there are tokens
            out = out.replace(token + token, token)
        return out
