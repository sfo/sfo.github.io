# %%
from typing import Any
import numpy as np
from numpy.typing import NDArray


# %%
def read_grid(filename: str) -> NDArray:
    with open(filename, "rt") as file:
        grid = np.array(list(zip(*file.readlines()))).T
    return grid


def fence_grid(grid: NDArray, fence_value: Any) -> NDArray:
    fenced = np.full((grid.shape[0] + 2, grid.shape[1] + 2), fence_value)
    fenced[1:-1, 1:-1] = grid
    return fenced


# %%
grid = fence_grid(read_grid("input.txt"), '.')
closed_list = {}
fences = {}
areas = {}


def process_region(grid, i, j, region_id) -> tuple[int, int]:
    x = grid[i, j]
    ij = complex(i, j)

    closed_list[ij] = region_id

    area = 1
    fence_count = 0
    for d in [1, 1j, -1, -1j]:
        nij = ij + d
        ni = int(nij.real)
        nj = int(nij.imag)
        if x == grid[ni, nj]:
            if nij in closed_list.keys():
                continue
            a, f = process_region(grid, ni, nj, region_id)
            area += a
            fence_count += f
        else:
            fence_count += 1
            fences[region_id] = fences.get(region_id, []) + [0.5 * (ij + nij)]
    return area, fence_count


def count_sides(fence: list[complex]) -> int:
    full_fence = fence.copy()
    side_count = 0
    while len(fence) > 0:
        side_count += 1
        ij = fence.pop()
        d_straight = ((ij.real % 1 == 0) * 1 + (ij.imag % 1 == 0) * 1j)
        d_cross = (1+1j) - d_straight

        for dir in [-1, +1]:
            for m in range(1, len(fence) + 1):
                nij = ij - dir * d_straight * m
                ij_cross_left = nij + dir * 0.5 * (d_straight + d_cross)
                ij_cross_right = nij + dir * 0.5 * (d_straight - d_cross)
                if (nij in fence) and not ((ij_cross_left in full_fence) or (ij_cross_right in full_fence)):
                    fence.remove(nij)
                else:
                    break
    return side_count


total_price = 0
region_id = 0
for i in range(1, grid.shape[0] - 1):
    for j in range(1, grid.shape[1] - 1):
        if complex(i, j) not in closed_list.keys():
            area, fence_count = process_region(grid, i, j, region_id)
            total_price += area * fence_count
            areas[region_id] = area
            region_id += 1

print("Solution for part 1 is:", total_price)

total_price = 0
for fence in fences.items():
    area = areas[fence[0]]
    side_count = count_sides(fence[1])
    total_price += area * side_count

print("Solution for part 2 is:", total_price)

# %%
