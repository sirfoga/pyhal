# !/usr/bin/python3
# coding: utf-8


""" Useful problems """


class EightQueen:
    """8 queen problem solver"""

    def __init__(self, board_size):
        self.board_size = board_size

    @staticmethod
    def under_attack(col, queens):
        """

        Args:
          col: int
        Column number
          queens: List of queens

        Returns:
          bool
          True iff queen is under attack

        """

        left = right = col
        for _, column in reversed(queens):
            left, right = left - 1, right + 1
            if column in (left, col, right):
                return True
        return False

    def solve(self, table_size):
        """

        Args:
          table_size: int
        Size of table

        Returns:
          List of possible solutions

        """

        if table_size == 0:
            return [[]]

        smaller_solutions = self.solve(table_size - 1)
        solutions = []
        for solution in smaller_solutions:
            for column in range(1, self.board_size + 1):
                # try adding a new queen to row = n, column = column
                if not self.under_attack(column, solution):
                    solutions.append(solution + [(table_size, column)])
        return solutions
