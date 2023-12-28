import re

lines = open(0).read().splitlines()

colors = ["red", "green", "blue"]
highest = [12, 13, 14]

ans = 0
for i, game in enumerate(lines):
    power = 1
    for color in colors:
        cnts = [int(x) for x in re.findall(f"(:?\d+) {color}", game)]
        power *= max(cnts)
    ans += power

print(ans)
