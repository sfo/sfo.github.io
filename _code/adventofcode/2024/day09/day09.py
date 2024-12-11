# %%
def decode_sectors(sectors: list[dict[str, int]]) -> list[int]:
    decoded_map = []
    for s in sectors:
        decoded_map += s["size"] * [s["id"]] + s["free"] * [-1]
    return decoded_map


def checksum(diskmap: list[int]) -> int:
    return sum([i * diskmap[i] for i in range(len(diskmap)) if diskmap[i] > 0])


def read_sectors() -> list[dict[str, int]]:
    with open("input.txt", "rt") as file:
        input = file.readlines()

    assert len(input) == 1
    input = input[0]
    return [
        {
            "id": id,
            "size": int(file_size),
            "free": int(gap_size),
        }
        for id, (file_size, gap_size) in enumerate(zip(input[::2], input[1::2] + "0"))
        # add 0 to account for final "virtual" gap
    ]


# %%
sectors = read_sectors()
diskmap = decode_sectors(sectors)
idx = len(diskmap) - 1
for id in range(len(diskmap)):
    while diskmap[idx] == -1:
        idx -= 1
    if id >= idx:
        break
    if diskmap[id] == -1:
        diskmap = (
            diskmap[:id]
            + [diskmap[idx]]
            + diskmap[id + 1 : idx]
            + [-1]
            + diskmap[idx + 1 :]
        )

print("Solution for part 1 is:", checksum(diskmap))

# %%
sectors = read_sectors()
i = len(sectors) - 1
while i > 0:
    for idx in range(i):
        if sectors[idx]["free"] >= sectors[i]["size"]:
            sectors[i - 1]["free"] += sectors[i]["size"] + sectors[i]["free"]
            sectors[i]["free"] = sectors[idx]["free"] - sectors[i]["size"]
            sectors[idx]["free"] = 0
            sectors = (
                sectors[: idx + 1]
                + [sectors[i]]
                + sectors[idx + 1 : i]
                + sectors[i + 1 :]
            )
            i += 1
            break
    i -= 1

diskmap = decode_sectors(sectors)

print("Solution for part 2 is:", checksum(diskmap))

# %%
