# %%
import re
import numpy as np


# %%
def execute_line(line: str) -> int:
    match = regex.findall(line)
    return np.sum([int(f1) * int(f2) for f1, f2 in match])


pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
regex = re.compile(pattern)

# %%
with open("input.txt", "r") as file:
    data = file.read()

result = execute_line(data)
print("Solution for part 1 is:", result)

# %% [markdown]
# # Part 2

# %%
with open("input.txt", "r") as file:
    data = file.read()

result = 0
splits = data.split("do")
for split in splits:
    if "n't" == split[:3]:
        continue
    result += execute_line(split)

print("Solution for part 2 is:", result)
