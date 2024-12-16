# %%
import numpy as np
from numpy.typing import NDArray
from typing import Any


# %%
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


# %%
def move(grid: NDArray, pos: complex, command: str) -> complex:
    moves = {
        '^': -1+0j,
        'v': +1+0j,
        '<':  0-1j,
        '>':  0+1j,
    }
    m = moves[command]
    if grid[idx(pos + m)] == 'O':
        move(grid, pos + m, command)
    if grid[idx(pos + m)] == '.':
        grid[idx(pos + m)] = grid[idx(pos)]
        grid[idx(pos)] = '.'
        return pos + m
    return pos


commands = ""
with open("input.txt", "rt") as file:
    grid = []
    while line := file.readline():
        if len(line) == 1:  # contains only newline
            break
        grid.append(line)

    while line := file.readline():
        commands += line[:-1]  # strip newline

    grid = np.array(list(zip(*grid))).T

pos = find_position(grid, "@")
for c in commands:
    pos = move(grid, pos, c)

print(
    "Solution for part 1 is:",
    sum([100 * i + j for i, j in zip(*(grid == 'O').nonzero())])
)

# %%
