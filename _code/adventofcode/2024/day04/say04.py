# %%
import re
import numpy as np


# %%
def count_matches(lines):
    pattern = r"XMAS"
    regex = re.compile(pattern)
    line = " ".join(lines)
    return len(regex.findall(line)) + len(regex.findall(line[::-1]))


def rot(arr, n):
    for _ in range(n):
        arr = np.rot90(arr)
    return arr


# %%
with open("input.txt") as f:
    lines = f.read().splitlines()

input = np.array(list(zip(*lines))).T
rotated_90 = rot(input, 1)

h, w = input.shape
diag_downwards = [input.diagonal(i) for i in range(-h + 1, w)]
diag_upwards = [np.flip(input, 1).diagonal(i) for i in range(-h + 1, w)]

print(
    "Solution for part 1 is:",
    np.sum(
        [
            count_matches(["".join(chars) for chars in arr])
            for arr in [input, rotated_90, diag_upwards, diag_downwards]
        ]
    ),
)

# %% [markdown]
#
# # Part 2

# %%
base_mask = np.array([
    ['M', np.nan, 'M'],
    [np.nan, 'A', np.nan],
    ['S', np.nan, 'S']
])

sum = 0
for i in range(0, h-2):
    for j in range(0, w-2):
        for n in range(4):
            mask = rot(base_mask, n)
            sum += (input[i:i+3, j:j+3] == mask).sum() == 5

print("Solution for part 2 is:", sum)
