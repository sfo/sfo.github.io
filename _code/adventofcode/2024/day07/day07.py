# %%
def check_equation(eq: list[int], ops) -> list[int]:
    if len(eq) == 1:
        return eq

    results = []
    for r in check_equation(eq[1:], ops):
        for op in ops:
            results.append(op(r, eq[0]))
    return results


input = []
with open("input.txt", "r") as file:
    while line := file.readline():
        line = line.split(":")
        result = int(line[0])
        equation = list(map(int, line[1].strip().split(" ")))
        input.append((result, equation))


# %%
result = sum(
    [
        r
        for r, equation in input
        if r
        in check_equation(
            list(reversed(equation)), [lambda a, b: a + b, lambda a, b: a * b]
        )
    ]
)

print("Solution for part 1:", result)

# %%
result = sum(
    [
        r
        for r, equation in input
        if r
        in check_equation(
            list(reversed(equation)),
            [lambda a, b: a + b, lambda a, b: a * b, lambda a, b: int(str(a) + str(b))],
        )
    ]
)

print("Solution for part 2:", result)

# %%
