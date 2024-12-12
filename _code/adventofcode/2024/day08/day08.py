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


def calculate_antinodes(antennas):
    antinodes = set()
    for i in range(len(antennas) - 1):
        for j in range(i + 1, len(antennas)):
            a = antennas[i]
            b = antennas[j]
            di = a[0] - b[0]
            dj = a[1] - b[1]

            antinodes.add((a[0] + di, a[1] + dj))
            antinodes.add((b[0] - di, b[1] - dj))
    return antinodes


def calculate_signal_impact(
    antinodes: set[tuple[int, int]], shape: tuple[int, int]
) -> int:
    return len(antinodes) - sum(
        [(i < 0 or j < 0 or i >= shape[0] or j >= shape[1]) for (i, j) in antinodes]
    )


# %%
with open("input.txt", "rt") as file:
    grid = np.array(list(zip(*file.readlines()))).T


# %%
antennas = find_antennas(grid)
antinodes = set()
for k, v in antennas.items():
    if len(v) > 1:
        antinodes = antinodes.union(calculate_antinodes(v))

print("Solution for part 1 is:", calculate_signal_impact(antinodes, grid.shape))

# %%
