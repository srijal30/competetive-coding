import re

testerfile = open('2', 'r')
content = testerfile.read()
testerfile.close()
lines = content.splitlines()

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