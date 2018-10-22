#!/usr/bin/env python
# coding: utf-8


"""Linked list implementation"""


class Node:
    """Node of a linked list"""

    def __init__(self, val, next_node=None):
        """
        :param val: Value of node
        :param next_node: Next node
        """
        self.val = val
        self.next_node = next_node  # the pointer initially points to nothing


class LinkedList:
    """Models a linked list"""

    def __init__(self, lst):
        """
        :param lst: List of elements
        """
        self.head = LinkedList.from_list(lst)

    def get_head(self):
        """Gets head

        :return: Head of linked list
        """
        return self.head

    def get(self, position):
        """Gets value at index

        :param position: index
        :return: value at position
        """

        counter = 0
        current_node = self.head

        while current_node is not None and counter <= position:
            if counter == position:
                return current_node.val

            current_node = current_node.next_node
            counter += 1

        return None

    def get_tail(self):
        """Gets tail

        :return: Tail of linked list
        """
        node = self.head
        last_node = self.head

        while node is not None:
            last_node = node
            node = node.next_node

        return last_node

    def length(self):
        """Gets length

        :return: How many items in linked list of linked list
        """
        item = self.head
        counter = 0

        while item is not None:
            counter += 1
            item = item.next_node

        return counter

    def insert_last(self, val):
        """Appends to list

        :param val: Object to insert
        :return: bool: Appends element to last
        """
        return self.insert(val, self.length())

    def insert_first(self, val):
        """Insert in head

        :param val: Object to insert
        :return: True iff insertion completed successfully
        """

        self.head = Node(val, next_node=self.head)
        return True

    def insert(self, val, position=0):
        """Insert in position

        :param val: Object to insert
        :param position: Index of insertion
        :return: bool: True iff insertion completed successfully
        """
        if position <= 0:  # at beginning
            return self.insert_first(val)

        counter = 0
        last_node = self.head
        current_node = self.head

        while current_node is not None and counter <= position:
            if counter == position:
                last_node.next_node = Node(val, current_node)
                return True

            last_node = current_node
            current_node = current_node.next_node
            counter += 1

        if current_node is None:  # append to last element
            last_node.next_node = Node(val, None)

        return True

    def remove_first(self):
        """Removes first

        :return: True iff head has been removed
        """

        if self.head is None:
            return False

        self.head = self.head.next_node
        return True

    def remove_last(self):
        """Removes last

        :return: True iff last element has been removed
        """

        if self.length() <= 1:
            self.head = None
            return True

        node = self.head

        while node is not None:
            is_last_but_one = node.next_node is not None and \
                              node.next_node.next_node is None
            print(node.val, is_last_but_one)
            if is_last_but_one:  # this is the last
                node.next_node = None  # get to last but one element
                return True

            node = node.next_node

        return False

    def remove(self, position):
        """Removes at index

        :param position: Index of removal
        :return: bool: True iff removal completed successfully
        """
        if position <= 0:  # at beginning
            return self.remove_first()

        if position >= self.length() - 1:  # at end
            return self.remove_last()

        counter = 0
        last_node = self.head
        current_node = self.head

        while current_node is not None and counter <= position:
            if counter == position:
                last_node.next_node = current_node.next_node  # remove current
                return True

            last_node = current_node
            current_node = current_node.next_node
            counter += 1

        return False

    def to_lst(self):
        """Cycle all items and puts them in a list

        :return: list representation
        """
        out = []
        node = self.head

        while node is not None:
            out.append(node.val)
            node = node.next_node

        return out

    def execute(self, func, *args, **kwargs):
        """Executes function on each item

        :param func: Function to execute on each item
        :param args: args of function
        :param kwargs: extra args of function
        :return: list: Results of calling the function on each item
        """
        return [
            func(item, *args, **kwargs) for item in self.to_lst()
        ]

    def __str__(self):
        lst = self.to_lst()
        lst = [
            str(node) for node in lst
        ]
        return " -> ".join(lst)

    @staticmethod
    def from_list(lst):
        """Parses list

        :param lst: list of elements
        :return: LinkedList: Nodes from list
        """
        if not lst:
            return None

        head = Node(lst[0], None)

        if len(lst) == 1:
            return head

        head.next_node = LinkedList.from_list(lst[1:])
        return head
