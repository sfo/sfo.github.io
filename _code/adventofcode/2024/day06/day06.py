# %%
import numpy as np
from numpy.typing import NDArray
from tqdm.auto import tqdm


# %%
def find_position(grid: NDArray) -> NDArray | None:
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell in "<>^v":
                return np.array([i, j])
    return None


def move(grid: NDArray, pos: NDArray) -> NDArray | None:
    moves = {
        "^": (np.array([-1, 0]), ">"),
        ">": (np.array([0, 1]), "v"),
        "v": (np.array([1, 0]), "<"),
        "<": (np.array([0, -1]), "^"),
    }
    dp, dd = moves[grid[*pos]]
    next_pos = pos + dp

    # return if leaving the grid
    if (next_pos < 0).any() or (next_pos > np.array(grid.shape) - 1).any():
        grid[*pos] = 'X'
        return None

    # rotate if next_pos is obstacle
    if grid[*next_pos] == "#":
        grid[*pos] = dd
        return pos

    grid[*next_pos] = grid[*pos]
    grid[*pos] = "X"
    return next_pos


# %%
with open("input.txt") as file:
    lines = file.read().splitlines()
    grid_master = np.array(list(zip(*lines))).T

grid = np.copy(grid_master)
p = find_position(grid)
steps = []
while p is not None:
    steps.append(p)
    p = move(grid, p)

print("Solution for part 1 is:", (grid == 'X').sum())


# %%
def check_obstacle(grid: NDArray, pos: NDArray) -> bool:
    grid_new = np.copy(grid)
    record = []
    p_start = p = find_position(grid_new)
    if (p_start == pos).all():
        return False
    # place new obstacle
    grid_new[*pos] = '#'
    # check new path
    while p is not None:
        if (tuple(p), grid_new[*p]) in record:
            # loop found
            return True
        record.append((tuple(p), grid_new[*p]))
        p = move(grid_new, p)
    return False


# %%
steps = np.unique(steps, axis=0)
loop_count = 0
for step in tqdm(steps):
    grid = np.copy(grid_master)
    if check_obstacle(grid, step):
        loop_count += 1

print("Solution for part 2 is:", loop_count)
