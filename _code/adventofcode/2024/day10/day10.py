# %%
import numpy as np


# %%
border_value = np.nan
with open("mini_example.txt", "rt") as file:
    map = np.array(list(zip(*file.readlines()))).T.astype(int)
    map = np.concat([np.full((map.shape[0], 1), border_value), map, np.full((map.shape[0], 1), border_value)], axis=1)
    map = np.concat([np.full((1, map.shape[1]), border_value), map, np.full((1, map.shape[1]), border_value)], axis=0)


def search_trails(map, i, j):
    if map[i, j] == 0:
        return [(i, j)]

    trails = []
    for d in [-1, 1]:
        if map[i + d][j] - map[i][j] == -1:
            trails += search_trails(map, i + d, j)
        if map[i][j + d] - map[i][j] == -1:
            trails += search_trails(map, i, j + d)
    return trails


for i in range(1, map.shape[0] - 1):
    for j in range(1, map.shape[1] - 1):
        if map[i, j] == 9:
            trails = search_trails(map, i, j)

trails