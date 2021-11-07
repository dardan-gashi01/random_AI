from typing import Optional

from PathfindingStrategy import PathfindingStrategy
from Utils import at_vector, is_valid_move
from Grid import Cell
from Grid import Moves
from Grid import Vector
from math import inf


class Dijkstra(PathfindingStrategy):

    def find_path(self, grid, start_pos, end_pos):

        at_vector(grid, start_pos).cost_from_root = at_vector(grid, start_pos).value

        to_do = [start_pos]
        while len(to_do) > 0:
            grid_location = to_do.pop(-1)

            if grid_location == end_pos:
                print("End located!")
                break

            grid_location_cell = at_vector(grid, grid_location)

            move_cost = {}

            # Go through every valid location next to our current location
            for move in Moves:
                new_pos = grid_location + move.value
                if is_valid_move(grid, new_pos):

                    # How much does the new tile cost? Got a +1 cause 0's
                    new_cost = grid_location_cell.cost_from_root + at_vector(grid, new_pos).value+1

                    # If that locations valid, tell it how close it is to the origin
                    if new_cost < at_vector(grid, new_pos).cost_from_root:
                        at_vector(grid, new_pos).cost_from_root = new_cost

                        # Also chuck it in the move_cost dict so we can keep track to 'to_do' it later
                        move_cost[move] = at_vector(grid, new_pos).cost_from_root

            # move_cost now has all movable tiles, let's order them by closest

            move_cost_cheapest_first = {k: v for k, v in sorted(move_cost.items(), key=lambda item: item[1], reverse=True)}
            for move_direction, cost in move_cost_cheapest_first.items():
                to_do.append(grid_location + move_direction.value)


        else:
            print("Path not found!")
            return grid

        # Backtracking
        to_do = [end_pos]

        while len(to_do) > 0:
            grid_location = to_do.pop(-1)
            at_vector(grid, grid_location).best_path = True

            if grid_location == start_pos:
                print("Start located!")
                break

            cheapest_direction = None
            cheapest_cost = inf

            for move in Moves:
                next_position = grid_location + move.value
                if is_valid_move(grid, next_position):

                    move_cost = at_vector(grid, next_position).cost_from_root

                    if move_cost < cheapest_cost:
                        cheapest_cost = move_cost
                        cheapest_direction = move

            to_do.append(grid_location + cheapest_direction.value)

        else:
            print("Something messed up.")
            return None

        return grid
