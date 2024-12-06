# %%
def check_rule(rules, line):
    rule = rules.get(line[0], [])
    for c in line[1:]:
        if c in rule:
            return False
    return True


# %%
rules = { }

sum = 0
with open("input.txt") as f:
    while len((line := f.readline().strip())) > 0:
        rule = line.split("|")
        rules[rule[1]] = rules.get(rule[1], []) + [rule[0]]

    while (line := f.readline().strip()):
        line = line.split(",")
        n = len(line)
        for i in range(n):
            if not check_rule(rules, line[i:]):
                break
        else:
            sum += int(line[len(line)//2])

print("Solution for part 1:", sum)


# %%