# use a memo
# basic plan on ipad

import re
lines = open(0).read().splitlines()


def possible(springs, groups):
    if len(groups) > 1:
        return 0



ans1 = 0
s = []
for i, l in enumerate(lines):
    springs, groups = l.split()
    s.append(len(springs))
    groups = list(map(int, groups.split(",")))
    """
    r1 = possible(springs, groups)
    r2 = possible("?".join([springs]*2), groups*2)
    r3 = possible("?"+springs, groups)
    r4 = possible(springs+"?", groups)
    mult = r2//r1
    print(i, "?".join([springs]*2), r1, mult, f"| {r3} {r4}")
    ans1 += r1*(mult**4)"""
print(max(s))
print(ans1)
