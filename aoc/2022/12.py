testerfile = open('12', 'r')
content = testerfile.read()
testerfile.close()
matrix = [[ord(x) for x in y] for y in content.splitlines()]
rows = len(matrix)
cols = len(matrix[0])

end = (0,0)
possibles = []
for x in range(rows):
    for y in range(cols):
        if matrix[x][y] == ord('S'):
            matrix[x][y] = ord('a')
            possibles.append((x,y))
        elif matrix[x][y] == ord('E'):
            matrix[x][y] = ord("z")
            end = (x,y)
        elif matrix[x][y] == ord('a'):
            possibles.append((x,y))

def valid(coord):
    return coord[0] >= 0 and coord[0] < rows and coord[1] >= 0 and coord[1] < cols

def reachable(coord1, coord2):
    return matrix[coord1[0]][coord1[1]]+1 >= matrix[coord2[0]][coord2[1]]

import math
def best_path(startX, startY):
    best_paths = {(x, y):math.inf for x in range(rows) for y in range(cols)}
    best_paths[(startX,startY)] = 0
    queue = [(startX,startY)]
    while len(queue) > 0:
        cur = queue.pop(0)
        curX = cur[0]
        curY = cur[1]
        up = (curX-1, curY)
        down = (curX+1, curY)
        left = (curX, curY-1)
        right = (curX, curY+1)
        if valid(up) and best_paths[cur] + 1 < best_paths[up] and reachable(cur, up):
            best_paths[up] = best_paths[cur] + 1
            queue.append(up)
        if valid(down) and best_paths[cur] + 1 < best_paths[down] and reachable(cur, down):
            best_paths[down] = best_paths[cur] + 1
            queue.append(down)
        if valid(left) and best_paths[cur] + 1 < best_paths[left] and reachable(cur, left):
            best_paths[left] = best_paths[cur] + 1
            queue.append(left)
        if valid(right) and best_paths[cur] + 1 < best_paths[right] and reachable(cur, right):
            best_paths[right] = best_paths[cur] + 1
            queue.append(right)
    return best_paths[end]

possibles = [best_path(*x) for x in possibles]
print(min(possibles))

