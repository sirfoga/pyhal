#!/usr/bin/env python
# coding: utf-8


"""Models to version stuff"""

from abc import abstractmethod

from hal.data.linked_list import LinkedList


class VersionNumber:
    """Version"""

    @abstractmethod
    def get_current_amount(self):
        """Gets current set amount

        :returns: Current set amount
        """
        pass

    def can_increase(self, amount):
        """Checks iff can increase by such amount

        :param amount: Amount to increase
        :returns: True iff this number can be increased by such amount
        """
        return amount <= self.max_amount_allowed()

    @abstractmethod
    def increase(self, amount=1):
        """Increase version by this amount

        :param amount: Increase number by this amount (Default value = 1)
        :returns: True iff increase was successful
        """
        pass

    @abstractmethod
    def maximize(self):
        """Maximizes this version"""
        pass

    @abstractmethod
    def reset(self):
        """Zeroes this number"""
        pass

    @abstractmethod
    def max_amount_allowed(self):
        """Calculates number of increases available

        :returns: Number of increases that can be done before reaching
        """
        pass

    @abstractmethod
    def max(self):
        """Calculates max increases

        :returns: Number of increases that can be done before reaching
        """
        pass


class Level(VersionNumber):
    """Level of version number"""

    def __init__(self, max_inner, start=0):
        """
        :param max_inner: Max number of this level. If you set to 0 this level will
            increase never
        :param start: Start at this number
        """
        self.max_inner = max_inner
        self.current = start

    def __str__(self):
        return str(self.current)

    def get_current_amount(self):
        """ """
        return self.current

    def increase(self, amount=1):
        """

        :param amount:  (Default value = 1)
        """
        if self.can_increase(amount):
            self.current += amount
            return True

        return False

    def maximize(self):
        """ """
        self.current = self.max_inner

    def reset(self):
        """ """
        self.current = 0

    def max_amount_allowed(self):
        """ """
        return self.max_inner - self.current

    def max(self):
        """ """
        return self.max_inner


class Subsystem(VersionNumber):
    """List of levels of version system"""

    def __init__(self, levels, separator="."):
        """
        :param levels: Levels in order of importance (from left to right the
            importance increases). The version number is the reversed
        :param separator: Compose version number separating with this split
        """
        self.ll = LinkedList(levels)
        self.current = self.max() - self.max_amount_allowed()  # inverse
        self.split = separator

    def __str__(self):
        out = [
            str(val) for val in self.ll.to_lst()
        ]
        out = self.split.join(reversed(out))  # reverse according importance
        return out

    def get_current_amount(self):
        """ """
        return self.current

    def reset(self):
        """ """
        node = self.ll.head

        while node is not None:
            node.val.reset()
            node = node.next_node

    def increase(self, amount=1):
        """

        :param amount:  (Default value = 1)
        """
        if self.ll.head.val.increase(amount):
            return True

        # head cannot increase -> reset and check for carry
        amount_left = amount - self.ll.head.val.max_amount_allowed() - 1
        self.ll.head.val.reset()

        node = self.ll.head.next_node
        carried = False

        while node is not None and not carried:
            if node.val.increase():
                carried = True
            else:
                node.val.reset()
            node = node.next_node

        if not carried:  # can't broadcast carry to last level
            return False

        return self.increase(amount_left)

    def maximize(self):
        """ """
        node = self.ll.head

        while node is not None:
            node.val.maximize()
            node = node.next_node

    def max_amount_allowed(self):
        """ """
        amount_allowed = self.ll.head.val.max_amount_allowed()
        multiplier = self.ll.head.val.max()
        node = self.ll.head.next_node

        while node is not None:
            amount_allowed += (node.val.max_amount_allowed() - 1) * multiplier
            multiplier *= node.val.max_inner
            node = node.next_node

        return amount_allowed

    def max(self):
        """ """
        multiplier = 1
        node = self.ll.head

        while node is not None:
            multiplier *= node.val.max()
            node = node.next_node

        return multiplier


class Version(VersionNumber):
    """Version"""

    def __init__(self, start="0.0.0", max_number=9, separator="."):
        """
        :param start: Current version
        :param max_number: Max number reachable by sub-versions numbers
        :param separator: Compose version number separating with this split
        """
        self.s = Version.from_str(start, max_number, separator)

    def __str__(self):
        return str(self.s)

    def get_current_amount(self):
        """ """
        return self.s.get_current_amount()

    def reset(self):
        """ """
        return self.s.reset()

    def max_amount_allowed(self):
        """ """
        return self.s.max_amount_allowed()

    def increase(self, amount=1):
        """

        :param amount:  (Default value = 1)
        """
        return self.s.increase(amount)

    def increase_by_changes(self, changes_amount, ratio):
        """Increase version by amount of changes

        :param changes_amount: Number of changes done
        :param ratio: Ratio changes
        :returns: Increases version accordingly to changes
        """
        increases = round(changes_amount * ratio)
        return self.increase(int(increases))

    def maximize(self):
        """ """
        return self.s.maximize()

    def max(self):
        """ """
        return self.s.max()

    @staticmethod
    def from_str(string, max_number=9, separator="."):
        """Parses string

        :param string: Version
        :param max_number: Max number reachable by sub (Default value = 9)
        :param separator: Version numbers are separated with this split (Default value = ".")
        :returns: Parses string and returns object
        """
        tokens = string.split(separator)
        tokens = list(reversed(tokens))  # reverse order of importance
        most_important = tokens[-1]  # cannot be parsed like the others
        levels = [
            Level(max_number, int(token)) for token in tokens[:-1]
        ]
        levels.append(
            Level(float("inf"), int(most_important))
        )

        return Subsystem(levels, separator)
