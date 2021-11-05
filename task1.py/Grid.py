from math import inf
import random
import matplotlib.pyplot as plt
from dataclasses import dataclass
from enum import Enum

@dataclass()
class Vector:
    x: int
    y: int
    
    def __add__(self, other):
        return Vector(self.x+other.x, self.y+other.y)


class Moves(Enum):
    UP = Vector(0, -1)
    DOWN = Vector(0, 1)
    LEFT = Vector(-1, 0)
    RIGHT = Vector(1, 0)


@dataclass
class Cell:
    value: int
    cost_from_root: int = inf
    best_path: bool = False


class Grid:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.grid = []

        self.cell_value_range = (0, 9)

        for y in range(self.height):
            row = []
            for x in range(self.width):
                row.append(Cell(random.randint(*self.cell_value_range)))
            self.grid.append(row)
#this function displays grid with random numbers filled
    def display(self):
        fig, ax = plt.subplots(figsize=(self.width, self.height))
        ax.axis("off")

        ax.matshow([[1 if x.best_path else 0 for x in y] for y in self.grid])

        for y in range(self.height):
            for x in range(self.width):
                cell = self.grid[y][x]
                ax.text(x, y, str(cell.value), va='center', ha='center')

        plt.show()
    #this function displays the path of the shortest path
    def pathfind(self, pathfinder):
        self.grid = pathfinder.find_path(self.grid,
                                         Vector(0, 0),
                                         Vector(len(self.grid[0])-1, len(self.grid)-1)
                                         )
