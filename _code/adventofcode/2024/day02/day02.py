# %%
import numpy as np


# %%
def is_save_report(levels):
    diff = levels[1:] - levels[:-1]

    return (
        np.sign(diff.min()) == np.sign(diff.max())
        and np.abs(diff).max() <= 3
        and np.abs(diff).min() >= 1
    )


# %%
sum = 0
with open("input.txt", "rt") as file:
    while line := file.readline():
        sequnce = np.array(line.split(), dtype=int)
        sum += is_save_report(sequnce)
sum

# %% [markdown]
# # Part 2

# %%
sum = 0
with open("input.txt", "rt") as file:
    while line := file.readline():
        sequnce = np.array(line.split(), dtype=int)
        for i in range(len(sequnce)):
            if is_save_report(np.concatenate([sequnce[0:i], sequnce[i + 1 :]])):
                sum += 1
                break

sum
