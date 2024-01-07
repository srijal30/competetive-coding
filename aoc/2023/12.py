# use a memo
# basic plan on ipad

import re
lines = open(0).read().splitlines()

memo = {}
def possible(springs, groups, cur):
    if (springs, groups, cur) in memo:
        return memo[(springs, groups, cur)]
    val = -1
    if len(groups) == 0:
        val = 1 if "#" not in springs else 0
    elif springs == "":
        if len(groups) == 0:
            val = 1
        elif len(groups) == 1:
            val = 1 if groups[0] == cur else 0
        else:
            val = 0
    elif springs[0] == ".":
        if cur == 0:
            val = possible(springs[1::], groups, 0)
        elif cur == groups[0]:
            val = possible(springs[1::], groups[1::], 0)
        else:
            val = 0
    elif springs[0] == "#":
        val = possible(springs[1::], groups, cur+1)
    elif springs[0] == "?":
        s1 = possible("."+springs[1::], groups, cur)
        s2 = possible("#"+springs[1::], groups, cur)
        val =  s1 + s2
    memo[(springs, groups, cur)] = val
    return val

ans1 = 0
s = []
for i, l in enumerate(lines):
    springs, groups = l.split()
    groups = tuple(map(int, groups.split(",")))
    r5 = possible("?".join([springs]*5), groups*5, 0)
    ans1 += r5

print(ans1)
