testerfile = open('8', 'r')
content = testerfile.read()
testerfile.close()

trees = [[int(x) for x in y] for y in content.splitlines()]
size = len(trees)

def valid_coord(x,y):
    return x >= 0 and y >= 0 and y < size and x < size

def find_score(X,Y):
    scores = [0 for i in range(4)]
    #up
    x = X-1
    y = Y
    while valid_coord(x,y):
        scores[0] +=1
        if trees[X][Y] <= trees[x][y]:
            break
        x-=1
    #left
    x = X
    y = Y-1
    while valid_coord(x,y):
        scores[1] +=1
        if trees[X][Y] <= trees[x][y]:
            break
        y-=1
    #down
    x = X+1
    y = Y
    while valid_coord(x,y):
        scores[2] +=1
        if trees[X][Y] <= trees[x][y]:
            break
        x+=1
    #right
    x = X
    y = Y+1
    while valid_coord(x,y):
        scores[3] +=1
        if trees[X][Y] <= trees[x][y]:
            break
        y+=1
    score = 1
    for s in scores:
        score *= s
    return score

highest = 0
for i in range(size):
    for j in range(size):
        highest = max(highest, find_score(i,j))
print(highest)