from Grid import Cell
from Grid import Vector


def is_valid_move(grid, location):
    return 0 <= location.x < len(grid[0]) and 0 <= location.y < len(grid)


def at_vector(grid, position):
    return grid[position.y][position.x]
