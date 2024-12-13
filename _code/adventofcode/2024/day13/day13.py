# %%
import re
import sympy as sp
from sympy.abc import a, b


# %%
def get_xy(line: str) -> tuple[int, int]:
    pattern = r"X\+(?P<X>\d+), Y\+(?P<Y>\d+)"
    regex = re.compile(pattern)
    match = regex.findall(line)
    return int(match[0][0]), int(match[0][1])


def get_prize(line: str) -> tuple[int, int]:
    pattern = r"X=(?P<X>\d+), Y=(?P<Y>\d+)"
    regex = re.compile(pattern)
    match = regex.findall(line)
    return int(match[0][0]), int(match[0][1])


def solve(input: list[str], offset: int) -> dict:
    x1, y1 = get_xy(input[0])
    x2, y2 = get_xy(input[1])
    xp, yp = get_prize(input[2])
    return sp.solve(
        [
            x1 * a + x2 * b - (xp + offset),
            y1 * a + y2 * b - (yp + offset),
        ],
        [a, b],
        dict=True,
    )


def count_tokens(a, b) -> int | None:
    if a.denominator == 1 and b.denominator == 1:
        return 3 * a + b
    return 0


with open("input.txt", "rt") as file:
    input = file.readlines()

print(
    "Solution for part 1 is:",
    sum(
        [
            count_tokens(s[a], s[b])
            for i in range(0, len(input), 4)
            for s in solve(
                input[i : i + 3],
                offset=0,
            )
        ]
    ),
)

print(
    "Solution for part 2 is:",
    sum(
        [
            count_tokens(s[a], s[b])
            for i in range(0, len(input), 4)
            for s in solve(
                input[i : i + 3],
                offset=10000000000000,
            )
        ]
    ),
)
