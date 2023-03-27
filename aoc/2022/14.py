testerfile = open('14', 'r')
content = testerfile.read()
testerfile.close()
steps = [[list(map(int,x.split(","))) for x in y.split(" -> ")] for y in content.splitlines()]
matrix = [['.' for y in range(600)] for x in range(200)]
# make the 2d array matrix
for step in steps:
    for i in range(len(step)-1):
        startX = step[i][0]
        startY = step[i][1]
        endX = step[i+1][0]
        endY = step[i+1][1]
        # print(range(startX, endX, 1 if endX-startX >= 0 else -1))
        # print(list(range(startY, endY, 1 if endY-startY >= 0 else -1)))
        for icol in range(startY, endY, 1 if endY-startY >= 0 else -1):
            for irow in range(startX, endX, 1 if endX-startX >= 0 else -1):
                pass

for x in range(0, 10):
    for y in range(494, 504):
        print(matrix[x][y], end="")
    print()