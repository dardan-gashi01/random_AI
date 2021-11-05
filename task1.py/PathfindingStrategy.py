from abc import ABC, abstractmethod
from typing import Optional
from Grid import Cell
from Grid import Vector


class PathfindingStrategy(ABC):

    @abstractmethod
    def find_path(self, grid, start_pos, end_pos):
        """
            Calculates and returns a list of coordinate's to travel from start to end of a grid.
            :param grid list[list[Cell]] 2d array containing Cell objects
            :param start_pos tuple[int, int] Contains an x,y pair of the starting position
            :param end_pos tuple[int, int] Contains an x,y pair of the starting position
            :return list[tuple[int, int]] | None
            """
        pass
