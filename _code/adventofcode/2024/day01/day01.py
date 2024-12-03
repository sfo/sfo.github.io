# %%
import pandas as pd
import numpy as np

# %%
df = pd.read_csv('input.txt', header=None, delimiter='\s+')
left = df[0]
right = df[1]

# %%
np.abs(left.sort_values().values - right.sort_values().values).sum()

# %% [markdown]
# # Part 2

# %%
counts = right.value_counts()
np.sum([i * (counts[i] if i in counts else 0) for i in left.values])
