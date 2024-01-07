grid = [[i for i in x] for x in open(0).read().splitlines()]
ans1 = 0

def tilt(grid):
    for r, row in enumerate(grid):
        for c, rock in enumerate(row):
            t = r
            swp = r
            while t < len(grid):
                if grid[t][c] == "#":
                    swp = t+1
                elif grid[t][c] == "O":
                    grid[t][c] = "."
                    grid[swp][c] = "O"
                    break
                t += 1
    return grid

def clockwise(grid):
    return [[grid[x][y] for x in range(len(grid))[::-1]] for y in range(len(grid[0]))]

def gridstr(grid):
    return "\n".join(["".join(x) for x in grid])

past = {}
j = 0
while True:
    for i in range(4):
        grid = tilt(grid)
        grid = clockwise(grid)
    key = gridstr(grid)
    if key in past:
        past[key].append(j)
        if len(past[key]) == 3:
            break
    else:
        past[key] = [j]
    j+=1

def find_load(gridstr):
    ans1 = 0
    grid = [[i for i in x] for x in gridstr.splitlines()]
    for r, row in enumerate(grid):
        power = len(row)-r
        for c, rock in enumerate(row):
            if rock == "O":
                ans1 += power

    return ans1

cycle_len = len([x for x in past if len(past[x]) >= 2])
for p in past:
    if len(past[p]) > 1 and (1000000000-past[p][0]-1)%cycle_len == 0:
        print(find_load(p))

