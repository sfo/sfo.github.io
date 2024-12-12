# %%
import numpy as np


# %%
def find_antennas(grid):
    antennas = {}
    for i, j in np.array(
        np.meshgrid(range(grid.shape[0]), range(grid.shape[1]))
    ).T.reshape(-1, 2):
        if grid[i, j] != ".":
            positions: list[tuple[int, int]] = antennas.get(grid[i, j], [])
            positions.append((i, j))
            antennas[grid[i, j]] = positions
    return antennas


def check_bounds(i, j, shape) -> bool:
    return not (i < 0 or j < 0 or i >= shape[0] or j >= shape[1])


def calculate_antinodes(antennas, shape, single):
    antinodes = set()
    for k in range(len(antennas) - 1):
        for l in range(k + 1, len(antennas)):
            a = antennas[k]
            b = antennas[l]
            di = a[0] - b[0]
            dj = a[1] - b[1]

            if single:
                if check_bounds(
                    antinode_i := a[0] + di,
                    antinode_j := a[1] + dj,
                    shape
                ):
                    antinodes.add((antinode_i, antinode_j))
                if check_bounds(
                    antinode_i := b[0] - di,
                    antinode_j := b[1] - dj,
                    shape
                ):
                    antinodes.add((antinode_i, antinode_j))
            else:
                for dx in [-1, 1]:
                    x = 0
                    while check_bounds(
                        antinode_i := a[0] + x * di,
                        antinode_j := a[1] + x * dj,
                        shape
                    ):
                        antinodes.add((antinode_i, antinode_j))
                        x += dx
                antinodes.add(a)
    return antinodes


# %%
with open("input.txt", "rt") as file:
    grid = np.array(list(zip(*file.readlines()))).T


# %%
antennas = find_antennas(grid)
antinodes = set()
for k, v in antennas.items():
    if len(v) > 1:
        antinodes = antinodes.union(calculate_antinodes(v, grid.shape, True))

print("Solution for part 1 is:", len(antinodes))

# %%
antennas = find_antennas(grid)
antinodes = set()
for k, v in antennas.items():
    if len(v) > 1:
        antinodes = antinodes.union(calculate_antinodes(v, grid.shape, False))

print("Solution for part 2 is:", len(antinodes))

# %%
