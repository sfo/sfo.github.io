# %%
from adventofcode.grid.algorithms import AStar
from adventofcode.grid.grid import find_position, idx, read_grid
import numpy as np
from numpy.typing import NDArray
from typing import override

from adventofcode.grid.grid import Grid


# %%
class Day16Grid(Grid):
    def __init__(self, grid: NDArray, finish: NDArray):
        super().__init__(grid)
        self._finish = finish

    @classmethod
    def rotation_to_direction(cls, rotation: int) -> NDArray:
        return np.array(
            [
                -np.sin(rotation * 0.5 * np.pi),
                np.cos(rotation * 0.5 * np.pi),
                0,
            ]
        ).astype(int)

    @override
    def expand_node(self, position: NDArray) -> list[NDArray]:
        neighbors = []
        # rotate left, right, or tuen around = move one / two level up or down (3rd dimension)
        for dl in [-1, 1, 2]:
            d = np.array([0, 0, dl])
            neighbor = position + d
            neighbor[2] = neighbor[2] % 4
            neighbors.append(neighbor)

        # make one step into direction of current rotation (if possible)
        dij = Day16Grid.rotation_to_direction(position[2])
        neighbor = position + dij
        if self._grid[*(position[:2])] != "#":
            neighbors.append(neighbor)

        return neighbors

    @override
    def is_finish(self, position: NDArray) -> bool:
        return (position[:2] == self._finish[:2]).all()

    @override
    def heuristic(
        self,
        position: NDArray,
        finish: NDArray | None = None,
    ) -> int:
        if finish is None:
            finish = self._finish

        if self.is_finish(position):
            return 0

        if np.equal(position[:2], finish[:2]).all():
            return 1000 * (((np.abs(finish[2] - position[2]) - 1) % 2) + 1)

        required_direction = np.sign(finish - position)[:2]
        current_direction = Day16Grid.rotation_to_direction(position[2])[:2]

        return (
            np.sum(np.abs(position - finish)[:2])
            + np.max(required_direction - current_direction) * 1000
        )


# %%
grid = read_grid("input.txt")
start = np.append(np.array(idx(find_position(grid, "S"))), 0)
finish = np.append(np.array(idx(find_position(grid, "E"))), np.nan)

day16grid = Day16Grid(grid, finish)
astar = AStar(day16grid)
path, cost = astar.search(start)
cost

# %%
