from abc import ABC, abstractmethod
from numpy.typing import NDArray
import numpy as np
from typing import Any


class Grid(ABC):
    def __init__(self, grid: NDArray):
        self._grid = grid

    @abstractmethod
    def expand_node(self, position: NDArray) -> list[NDArray]:
        pass

    @abstractmethod
    def is_finish(self, position) -> bool:
        pass

    @abstractmethod
    def heuristic(
        self,
        position: NDArray,
        finish: NDArray | None = None,
    ) -> int:
        pass


def read_grid(filename: str) -> NDArray:
    with open(filename, "rt") as file:
        grid = np.array(list(zip(*file.readlines()))).T
    return grid


def fence_grid(grid: NDArray, fence_value: Any) -> NDArray:
    fenced = np.full((grid.shape[0] + 2, grid.shape[1] + 2), fence_value)
    fenced[1:-1, 1:-1] = grid
    return fenced


def idx(ij: complex) -> tuple[int, int]:
    i = int(ij.real)
    j = int(ij.imag)
    return (i, j)


def iter_grid(grid: NDArray) -> complex:
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            yield complex(i, j)


def find_position(grid: NDArray, value: Any) -> complex | None:
    for ij in iter_grid(grid):
        if grid[idx(ij)] == value:
            return ij
    return None
