testerfile = open('16', 'r')
content = testerfile.read()
testerfile.close()
lines = content.splitlines()

time = 30
pipes = {}
paths = {}

time = 30
for line in lines:
    pipes[line[6:8]] = int(line.split("rate=")[1].split(";")[0])
    paths[line[6:8]] = line.split("valves ")[-1].split(", ")

import sys
sys.setrecursionlimit(10000)
def max_pressure(cur, opened, time):
    # base cases
    if time == 0:
       return 0
    if len(opened) == len(paths):
        return 0
    
    curBest = 0
    for path in paths[cur]:
        # if we open current pipe
        if cur not in opened:
            val = max_pressure(path, opened + [cur], time-2) + (time-1)*pipes[cur]
            curBest = max(curBest, val)
        # if we dont open current pipe
        curBest = max(curBest, max_pressure(path, opened, time-1))

    return curBest

print(max_pressure("AA", [], 30))
print("hi")

exit()
print("\t", end="")
for y in range(1, time+1):
    print(y, end="\t")
print()
for x in pipes:
    print(x, end=": ")
    for y in reversed(range(time)):
        print(pipes[x]*y, end="\t")
    print()

