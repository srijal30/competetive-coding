grid = [l for l in open(0).read().splitlines()]
n = len(grid)

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == "S":
            start = (i,j)
            break
        else:
            continue
        break

moves = {(-1,0):"|LJ", (1,0):"|7F", (0,-1):"-J7", (0,1):"-LF"}
pipes = set("|-LJ7F")
for m in moves:
    nx = start[0] + m[0]
    ny = start[1] + m[1]
    if nx not in range(n) or ny not in range(n):
        continue
    if grid[nx][ny] in moves[(m[0]*-1, m[1]*-1)]:
        pipes &= set(moves[m])

assert len(pipes) == 1
grid[start[0]] = grid[start[0]].replace("S", pipes.pop())
    
visited = set()
queue = [start]
while len(queue) != 0:
    cur = queue.pop(0)
    x, y = cur
    for m in moves:
        nx = x + m[0]
        ny = y + m[1]
        if nx not in range(len(grid)) or ny not in range(len(grid[0])):
                continue
        if grid[x][y] in moves[m] and (nx, ny) not in visited:
            queue.append((nx, ny))
            visited.add((nx,ny))

print(len(visited)//2)

ans2 = 0
for i in range(len(grid)):
    cnt = 0
    st = 0
    nd = 0
    for j in range(len(grid[i])):
        if (i, j) in visited and grid[i][j] == "|":
            cnt += 1
        elif (i, j) in visited and st == 0:
            if grid[i][j] in "7F":
                st = -1
            elif grid[i][j] in "JL":
                st = 1
        elif (i, j) in visited and st != 0 and grid[i][j] in "7FJL":
            if grid[i][j] in "7F":
                nd = -1
            elif grid[i][j] in "JL":
                nd = 1
            if nd * st < 0:
                cnt += 1
            nd = 0
            st = 0
        elif (i,j) not in visited:
            if cnt % 2 == 1:
                ans2 += 1

print(ans2)


