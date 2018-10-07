#!/usr/bin/env python
# coding: utf-8


""" Models to version stuff """

from abc import abstractmethod

from hal.data.linked_list import LinkedList


class VersionNumber:
    """ """

    @abstractmethod
    def get_current_amount(self):
        """
        Gets current set amount

        Returns: Current set amount
        """
        pass

    def can_increase(self, amount):
        """
        Args:
            amount: Amount to increase

        Returns: True iff this number can be increased by such amount
        """
        return amount <= self.max_amount_allowed()

    @abstractmethod
    def increase(self, amount=1):
        """
        Increase version by this amount

        Args:
            amount: Increase number by this amount (Default value = 1)

        Returns: True iff increase was successful
        """
        pass

    @abstractmethod
    def maximize(self):
        """
        Maximizes this version

        Returns: Maximizes this version
        """
        pass

    @abstractmethod
    def reset(self):
        """
        Zeroes this number

        Returns: Zeroes this number
        """
        pass

    @abstractmethod
    def max_amount_allowed(self):
        """
        Calculates number of increases available

        Returns: Number of increases that can be done before reaching maximum
        """
        pass

    @abstractmethod
    def max(self):
        """
        Calculates max increases

        Returns: Number of increases that can be done before reaching maximum
            starting at 0
        """
        pass


class Level(VersionNumber):
    """Level of version number"""

    def __init__(self, max_inner, start=0):
        """
        Args
            max_inner: Max number of this level. If you set to 0 this level will
                increase never
            start: Start at this number
        """
        self.max_inner = max_inner
        self.current = start

    def __str__(self):
        return str(self.current)

    def get_current_amount(self):
        """
        Gets current amount

        Returns: Current amount
        """
        return self.current

    def increase(self, amount=1):
        """
        Increases version by this amount

        Args:
            amount: amount to increase by
        Returns: Increases version by this amount
        """
        if self.can_increase(amount):
            self.current += amount
            return True

        return False

    def maximize(self):
        """
        Maximizes this version

        Returns: Maximizes this version
        """
        self.current = self.max_inner

    def reset(self):
        """
        Resets this version

        Returns: Resets this version
        """
        self.current = 0

    def max_amount_allowed(self):
        """
        Gets max amounts of version

        Returns: Gets max amounts of version
        """
        return self.max_inner - self.current

    def max(self):
        """
        Gets max of version

        Returns: Gets max of version
        """
        return self.max_inner


class Subsystem(VersionNumber):
    """List of levels of version system"""

    def __init__(self, levels, separator="."):
        """
        Args:
            levels: Levels in order of importance (from left to right the
                importance increases). The version number is the reversed
            separator: Compose version number separating with this split
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
        """
        Gets current amount

        Returns: Current amount
        """
        return self.current

    def reset(self):
        """
        Resets version

        Returns: Resets version
        """
        node = self.ll.head

        while node is not None:
            node.val.reset()
            node = node.next_node

    def increase(self, amount=1):
        """
        Increases version

        Args:
          amount: amount to increase version by

        Returns: Increases version
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
        """
        Maximizes version

        Returns: Maximizes version
        """
        node = self.ll.head

        while node is not None:
            node.val.maximize()
            node = node.next_node

    def max_amount_allowed(self):
        """
        Calculates number of increases available

        Returns: Number of increases that can be done before reaching maximum
        """
        amount_allowed = self.ll.head.val.max_amount_allowed()
        multiplier = self.ll.head.val.max()
        node = self.ll.head.next_node

        while node is not None:
            amount_allowed += (node.val.max_amount_allowed() - 1) * multiplier
            multiplier *= node.val.max_inner
            node = node.next_node

        return amount_allowed

    def max(self):
        """
        Maximizes this version

        Returns: Maximizes this version
        """
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
        Args:
            start:  Current version
            max_number: Max number reachable by sub-versions numbers
            separator: Compose version number separating with this split
        """
        self.s = Version.from_str(start, max_number, separator)

    def __str__(self):
        return str(self.s)

    def get_current_amount(self):
        """ """
        return self.s.get_current_amount()

    def reset(self):
        """
        Zeroes this number

        Returns: Zeroes this number
        """
        return self.s.reset()

    def max_amount_allowed(self):
        """
        Calculates number of increases available

        Returns: Number of increases that can be done before reaching maximum
        """
        return self.s.max_amount_allowed()

    def increase(self, amount=1):
        """
        Increase version by this amount

        Args:
            amount: Increase number by this amount (Default value = 1)

        Returns: True iff increase was successful
        """
        return self.s.increase(amount)

    def increase_by_changes(self, changes_amount, ratio):
        """
        Increase version by amount of changes

        Args:
          changes_amount: Number of changes done
          ratio: Ratio changes / version increases

        Returns: Increase version accordingly to changes
        """
        increases = round(changes_amount * ratio)
        return self.increase(int(increases))

    def maximize(self):
        """
        Maximizes this version

        Returns: Maximizes this version
        """
        return self.s.maximize()

    def max(self):
        """
        Calculates max increases

        Returns: Number of increases that can be done before reaching maximum
            starting at 0
        """
        return self.s.max()

    @staticmethod
    def from_str(string, max_number=9, separator="."):
        """
        Parses string

        Args:
          string: Version
          max_number: Max number reachable by sub-versions numbers
          separator: Version numbers are separated with this split

        Returns: Parses string and returns object
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
