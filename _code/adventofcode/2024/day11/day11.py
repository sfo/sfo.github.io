# %%
from functools import lru_cache


# %%
@lru_cache(maxsize=102400)
def transform_stone(stone: int) -> int | tuple[int, int]:
    if stone == 0:
        return 1
    num_len = len(str(stone))
    if num_len % 2 == 0:
        x = 10 ** (num_len // 2)
        return stone // x, stone % x
    return stone * 2024


def flatten(stones: int | list[int | list[int] | tuple[int]]) -> tuple[int]:
    result = []
    if isinstance(stones, int):
        return (stones, )

    for s in stones:
        if isinstance(s, list) or isinstance(s, tuple):
            for sub_s in s:
                result.append(sub_s)
        else:
            result.append(s)
    return tuple(result)


@lru_cache(maxsize=102400)
def blink(stones: tuple[int], n_blink: int) -> int:
    if n_blink == 0:
        return len(stones)

    if len(stones) == 1:
        stones = flatten(transform_stone(stones[0]))
        return blink(stones, n_blink-1)

    return sum([
        blink((stone,), n_blink) for stone in stones
    ])


# %%
with open("input.txt", "rt") as file:
    input = file.readlines()
    assert len(input) == 1
    stones = tuple(map(int, input[0].split(" ")))

# %%
n_blink = 25
stone_count = blink(stones, n_blink)
print("Solution for part 1 is:", stone_count)

# %%
n_blink = 75
stone_count = blink(stones, n_blink)
print("Solution for part 2 is:", stone_count)

# %%
