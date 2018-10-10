#!/usr/bin/env python
# coding: utf-8


"""Linked list implementation """


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
        
        :returns: Head of linked list
        """
        return self.head

    def get_tail(self):
        """Gets tail
        
        :returns: Tail of linked list
        """
        node = self.head
        last_node = self.head

        while node is not None:
            last_node = node
            node = node.next_node

        return last_node

    def length(self):
        """Gets length
        
        :returns: How many items in linked list of linked list
        """
        item = self.head
        counter = 0

        while item is not None:
            counter += 1
            item = item.next_node

        return counter

    def append(self, val):
        """Appends to list

        :param val: Object to insert
        :returns: bool: Appends element to last
        """
        return self.insert(val, self.length())

    def insert(self, val, at=0):
        """Insert in position

        :param val: Object to insert
        :param at: Index of insertion (Default value = 0)
        :returns: bool: True iff insertion completed successfully
        """
        if at < 0 or at > self.length():
            return False

        if at == 0:  # at beginning
            self.head = Node(val, next_node=self.head)
            return True

        counter = 0
        last_node = self.head
        current_node = self.head

        while current_node is not None and counter <= at:
            if counter == at:
                last_node.next_node = Node(val, current_node)
                return True

            last_node = current_node
            current_node = current_node.next_node
            counter += 1

        if current_node is None:  # append to last element
            last_node.next_node = Node(val, None)
            return True

        return False

    def remove_first(self):
        """Removes first
        
        :returns: True iff head has been removed
        """
        if self.head.next_node is not None:
            self.head = self.head.next_node
            return True

        return False

    def remove_last(self):
        """Removes last
        
        :returns: True iff last element has been removed
        """
        node = self.head

        while node is not None:
            if node.next_node.next_node is None:
                node.next_node = None  # get to last but one element
                return True

            node = node.next_node

        return False

    def remove(self, at):
        """Removes at index

        :param at: Index of removal
        :returns: bool: True iff removal completed successfully
        """
        if at < 0 or at > self.length():
            return False

        if at == 0:  # at beginning
            self.remove_first()

        if at == self.length():  # at end
            self.remove_last()

        counter = 0
        last_node = self.head
        current_node = self.head

        while current_node is not None and counter <= at:
            if counter == at:
                last_node.next_node = current_node.next_node  # remove current
                return True

            last_node = current_node
            current_node = current_node.next_node
            counter += 1

        return False

    def to_lst(self):
        """Cycle all items and puts them in a list
        
        :returns: list representation
        """
        out = []
        node = self.head

        while node is not None:
            out.append(node.val)
            node = node.next_node

        return out

    def execute(self, func):
        """Executes function on each item

        :param func: Function to execute on each item
        :returns: list: Results of calling the function on each item
        """
        return [
            func(item) for item in self.to_lst()
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
        :returns: LinkedList: Nodes from list
        """
        if not lst:
            return None

        head = Node(lst[0], None)

        if len(lst) == 1:
            return head

        head.next_node = LinkedList.from_list(lst[1:])
        return head
