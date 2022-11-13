size = int(input())

grid = []
for x in range(size):
    grid.append([])
    io = input()
    for y in range(size):
        grid[x].append(io[y])

nums_grid = grid.copy()

for x in range(size):
    for y in range(size):
        if grid[x][y] != ".":
            nums_grid[x][y] = 0
        elif x == 0 and y == 0:
            nums_grid[x][y] = 1
        elif x == 0:
            nums_grid[x][y] = nums_grid[x][y-1]
        elif y == 0:
            nums_grid[x][y] = nums_grid[x-1][y]
        else:
            nums_grid[x][y] = nums_grid[x-1][y] + nums_grid[x][y-1]

print(nums_grid[size-1][size-1])


