# %%
from typing import override
from adventofcode.grid.algorithms import AStar
from adventofcode.grid.grid import Grid, read_grid
import numpy as np
from numpy.typing import NDArray


# %%
class Day18Grid(Grid):
    def __init__(self, grid: NDArray, finish: NDArray):
        super().__init__(grid)
        self._finish = finish

    @override
    def expand_node(self, position: NDArray) -> list[NDArray]:
        neighbors = []
        # in each dimension, do one step in each direction (if possible)
        for dim in [0, 1]:
            d = np.zeros_like(position)
            for step in [-1, 1]:
                d[dim] = step
                neighbor = position + d

                if (neighbor < 0).any() or (neighbor >= self._grid.shape).any():
                    continue

                if self._grid[*position] != "#":
                    neighbors.append(neighbor)

        return neighbors

    @override
    def is_finish(self, position: NDArray) -> bool:
        return (position == self._finish).all()

    @override
    def heuristic(
        self,
        position: NDArray,
        finish: NDArray | None = None,
    ) -> int:
        if finish is None:
            finish = self._finish
        return np.sum(np.abs(finish - position))


# %%
# filename = "example.txt"
# grid_size = 7
# byte_count = 12

filename = "input.txt"
grid_size = 71
byte_count = 1024

grid = np.full(shape=(grid_size, grid_size), fill_value=".")
with open(filename, "rt") as file:
    while (line := file.readline()) and byte_count > 0:
        xy = line.split(",")
        grid[int(xy[1]), int(xy[0])] = '#'
        byte_count -= 1

grid

# %%
start = np.array([0, 0])
finish = np.array(grid.shape) - 1

day18grid = Day18Grid(grid, finish)
astar = AStar(day18grid)
path, cost = astar.search(start)
cost

# %%
