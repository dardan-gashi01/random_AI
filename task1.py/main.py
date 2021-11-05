from Grid import Grid
from Dijkstra import Dijkstra


def main():
    grid = Grid(10,10)
    grid.pathfind(Dijkstra())
    grid.display()


if __name__ == "__main__":
    main()
