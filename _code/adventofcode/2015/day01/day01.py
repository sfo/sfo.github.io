# %%
test_cases = [
    ("(())", 0),
    ("()()", 0),
    ("(((", 3),
    ("(()(()(", 3),
    ("))(((((", 3),
    ("())", -1),
    ("))(", -1),
    (")))", -3),
    (")())())", -3),
]


def get_floor(map: str) -> int:
    return int(eval(map.replace("(", "+1").replace(")", "-1")))


for test in test_cases:
    assert test[1] == get_floor(test[0])


with open("input.txt", "rt") as file:
    input = file.readline()

print("Solution for part 1 is:", get_floor(input))

# %%
level = 0
for i, c in enumerate(input):
    level += 1 if c == "(" else -1
    if level < 0:
        print("Solution for part 2 is:", i+1)
        break