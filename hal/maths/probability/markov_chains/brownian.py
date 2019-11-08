import random
from enum import Enum


class Direction(Enum):
    NORTH = 1
    EAST = 2
    SOUTH = 3
    WEST = 4
    NULL = 5


POSSIBLE_DIRECTIONS = [
    Direction.NORTH, Direction.EAST, Direction.SOUTH, Direction.WEST
]


def direction2coords(direction, step_size=1):
    if direction == Direction.NORTH:
        return 0, 1 * step_size

    if direction == Direction.EAST:
        return 1 * step_size, 0

    if direction == Direction.SOUTH:
        return 0, -1 * step_size

    if direction == Direction.WEST:
        return -1 * step_size, 0

    return 0, 0  # stay here


class LatticePoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add_direction(self, direction):
        x, y = direction2coords(direction)
        new_x = self.x + x
        new_y = self.y + y
        return LatticePoint(new_x, new_y)

    @staticmethod
    def origin():
        return LatticePoint(0, 0)


def next_direction(n_people=1):
    """
    If all people agree, take that direction. Otherwise stay there

    :param n_people: number of people choosing the direction
    :return: one of POSSIBLE_DIRECTIONS
    """

    if n_people <= 1:
        return random.choice(POSSIBLE_DIRECTIONS)

    # common direction only if all people agree
    n_directions = [
        next_direction() for _ in range(n_people)
    ]
    common_direction = n_directions[0]
    for direction in n_directions:
        if direction != common_direction:
            return Direction.NULL

    return common_direction


def simulate_trajectory(n_people, time):
    return [
        next_direction(n_people)
        for _ in range(time)  # discreet time
    ]


def points_trajectory(directions, start=LatticePoint.origin()):
    points = [start]

    for direction in directions:
        new_point = points[-1].add_direction(direction)
        points.append(new_point)

    return points
