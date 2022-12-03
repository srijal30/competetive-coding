def plus(list, cnt):
    return [(x+cnt-1)%9+1 for x in list]


content = open("day15test.txt", "r").read()

small_matrix = [[int(x) for x in y] for y in content.splitlines()]
bigger_matrix = []

for x in range(len(small_matrix)):
    bigger_matrix.append([])
    for length in range(5):
        bigger_matrix[x] += plus(small_matrix[x],length)

matrix = []
for x in range(5):
    for y in range(len(bigger_matrix)):
        matrix.append(plus(bigger_matrix[y], x))

size = len(matrix)

def valid(coord):
    return coord[0] >= 0 and coord[0] < size and coord[1] >= 0 and coord[1] < size

import math
best_paths = {(x, y):math.inf for x in range(size) for y in range(size)}
best_paths[(0,0)] = 0
queue = [(0,0)]


while len(queue) > 0:
    cur = queue.pop(0)
    curX = cur[0]
    curY = cur[1]

    up = (curX-1, curY)
    down = (curX+1, curY)
    left = (curX, curY-1)
    right = (curX, curY+1)

    if valid(up) and best_paths[cur] + matrix[curX-1][curY] < best_paths[up]:
        best_paths[up] = best_paths[cur] + matrix[curX-1][curY]
        queue.append(up)

    if valid(down) and best_paths[cur] + matrix[curX+1][curY] < best_paths[down]:
        best_paths[down] = best_paths[cur] + matrix[curX+1][curY]
        queue.append(down)

    if valid(left) and best_paths[cur] + matrix[curX][curY-1] < best_paths[left]:
        best_paths[left] = best_paths[cur] + matrix[curX][curY-1]
        queue.append(left)

    if valid(right) and best_paths[cur] + matrix[curX][curY+1] < best_paths[right]:
        best_paths[right] = best_paths[cur] + matrix[curX][curY+1]
        queue.append(right)

"""
for x in range(size):
    for y in range(size):
        print(best_paths[(x,y)], end=" ")
    print()
"""

print(best_paths[(size-1, size-1)])
