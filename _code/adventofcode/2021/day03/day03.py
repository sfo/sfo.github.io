# %%
import pandas as pd
import numpy as np
import decimal


# %%
def round(f):
    return decimal.Decimal(f).quantize(decimal.Decimal('0'), rounding=decimal.ROUND_HALF_UP)


# %%
def binary_list_to_int(l):
    return int(sum(2**i * v for i, v in enumerate(reversed(l))))


# %%
# df = pd.read_fwf("example.txt", header=None, widths=5*[1])
df = pd.read_fwf("input.txt", header=None, widths=12*[1])

# %%
binary = df.mean(axis="rows").round(0)
gamma = binary_list_to_int(binary)
epsilon = binary_list_to_int([1-v for v in binary])
print("Part one solution is:", gamma * epsilon)

# %% [markdown]
# # Part 2

# %%
selection = df.copy()
while len(selection) > 1:
    most_common_bit = int(round(selection.iloc[:, 0].mean()))
    selection = selection[selection.iloc[:, 0] == most_common_bit].iloc[:, 1:]
oxygen_generator_rating = binary_list_to_int(df.iloc[selection.index[0]].values)
oxygen_generator_rating

# %%
selection = df.copy()
while len(selection) > 1:
    least_common_bit = 1 - int(round(selection.iloc[:, 0].mean()))
    selection = selection[selection.iloc[:, 0] == least_common_bit].iloc[:, 1:]
co2_scrubber_rating = binary_list_to_int(df.iloc[selection.index[0]].values)
co2_scrubber_rating

# %%
print("Part two solution is:", oxygen_generator_rating * co2_scrubber_rating)