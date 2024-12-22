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


def create_grid(size: int, fallen_bytes: NDArray) -> NDArray:
    grid = np.full(shape=(size, size), fill_value=".")
    for b in fallen_bytes:
        grid[*b] = "#"
    return grid.T


def search_path(grid: NDArray) -> int:
    start = np.array([0, 0])
    finish = np.array(grid.shape) - 1

    day18grid = Day18Grid(grid, finish)
    astar = AStar(day18grid)
    _, cost = astar.search(start)
    return cost


def bisect(start_byte, end_byte) -> int | None:
    center_byte = (start_byte + end_byte) // 2
    grid = create_grid(grid_size, fallen_bytes[:center_byte])
    cost = search_path(grid)
    if np.isnan(cost):
        if end_byte == center_byte:
            return None
        return bisect(start_byte, center_byte)
    if center_byte == start_byte:
        return center_byte
    return bisect(center_byte, end_byte)


# %% [markdown]
# # Common
#
# %%
with open("input.txt", "rt") as file:
    fallen_bytes = np.array([line.split(",") for line in file.readlines()], dtype=int)

# %% [markdown]
#
# # PART 1
#
# %%
byte_count = 1024
grid_size = 71

grid = create_grid(grid_size, fallen_bytes[:byte_count])
print("Solution for part 1 is:", search_path(grid))

# %% [markdown]
#
# # PART 2
#
# %%
print("Solution for part 2 is:", fallen_bytes[bisect(byte_count, len(fallen_bytes))])
