# %%
import pandas as pd
import numpy as np

# %%
sum = 50
count_rest_on_zero = 0
count_turns_over_zero = 0

with open("input.txt", "rt") as file:
    while line := file.readline():
        print(line, end='')
        s = -1 if line[0] == "L" else +1
        new_sum = (sum + s * int(line[1:]))
        print(f"  -> previous sum = {sum}, new sum = {new_sum}")

        if new_sum > 100:
            count_turns_over_zero += (new_sum // 100)
            if new_sum % 100 == 0:
                count_turns_over_zero -= 1
            print(f"  -> zeros = {new_sum // 100}")
        if new_sum < 0 and sum != 0:
            count_turns_over_zero += abs(new_sum // 100)
            print(f"  -> zeros = {abs(new_sum // 100)}")

        new_sum = new_sum % 100
        print(f"  -> final new sum = {new_sum}")
        if new_sum == 0:
            count_rest_on_zero += 1
            count_turns_over_zero += 1
            print(f"  -> rest on zero")

        sum = new_sum


print(f"How often the dial rests on zero: {count_rest_on_zero}")
print(f"How often the dial turns over zero: {count_turns_over_zero}")

# %%
# it's not
#   5562
#   5467
#