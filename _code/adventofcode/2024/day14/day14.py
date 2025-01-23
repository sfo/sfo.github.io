# %%
import re
from collections import Counter
from functools import reduce
import numpy as np
from tqdm.auto import tqdm


# %%
# maxx = 11
# maxy = 7
# input_file = "example.txt"

maxx = 101
maxy = 103
input_file = "input.txt"


def visualize(positions: list[tuple[int, int]]):
    grid = np.zeros((maxy, maxx))
    for (x, y) in positions:
        grid[y, x] += 1
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            print('#' if grid[i, j] > 0 else ' ', end='')
        print()


with open(input_file, "rt") as file:
    input = file.readlines()

pattern = r"p=(\d+),(\d+) v=(-?\d+),(-?\d+)"
regex = re.compile(pattern)

# %%
seconds = 100
dx = maxx // 2
dy = maxy // 2
c = Counter()
for line in input:
    match = regex.findall(line)[0]
    x = (int(match[0]) + seconds * int(match[2])) % maxx
    y = (int(match[1]) + seconds * int(match[3])) % maxy
    if x == dx or y == dy:
        continue
    c[(x < dx) * 10 + (y < dy)] += 1

print(
    "Solution for part 1 is:",
    reduce(lambda x, y: x*y, c.values(), 1)
)

# %%
seconds = 0
for _ in tqdm(range(maxx*maxy)):
    cx = Counter()
    cy = Counter()
    positions = []
    for line in input:
        match = regex.findall(line)[0]
        x = (int(match[0]) + seconds * int(match[2])) % maxx
        y = (int(match[1]) + seconds * int(match[3])) % maxy
        positions += [(x, y)]
        cx[x] += 1
        cy[y] += 1

    q = 4
    if cx.most_common(1)[0][1] > maxx / q and cy.most_common(1)[0][1] > maxy / q:
        break

    seconds += 1

print("After", seconds, "seconds, the robots form the following image:")
visualize(positions)