# %%
def decode_diskmap(map: str) -> list[int]:
    id = 0
    decoded_map = []
    for i in range(len(map)):
        if i % 2 == 0:  # file
            decoded_map += int(map[i]) * [id]
            id += 1
        else:  # empty
            decoded_map += int(map[i]) * [-1]
    return decoded_map


# %%
with open("input.txt", "rt") as file:
    input = file.readlines()
    assert len(input) == 1
    input = decode_diskmap(input[0])

# %%
j = len(input) - 1
for i in range(len(input)):
    while input[j] == -1:
        j -= 1
    if i >= j:
        break
    if input[i] == -1:
        input = input[:i] + [input[j]] + input[i+1:j] + [-1] + input[j+1:]

print("Solution for part 1 is:", sum([i * input[i] for i in range(len(input)) if input[i] > 0]))

# %%
