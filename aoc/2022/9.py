testerfile = open('9', 'r')
content = testerfile.read()
testerfile.close()
lines = content.splitlines()

queue = []
def add_moves(dir, amnt):
    move = (0,0)
    if dir == "R":
        move = (1,0)
    elif dir == "L":
        move = (-1,0)
    elif dir == "U":
        move = (0,1)
    elif dir == "D":
        move = (0,-1)
    for x in range(int(amnt)):
        queue.append(move)        

# get all the moves
for line in lines:
    dir, amnt = line.split(" ")
    add_moves(dir, amnt)

# move the head and tail
visited = []
snake = [(0,0) for x in range(10)]

# returns the new tail position
def move_tail(head, tail):
    headX = head[0]
    headY = head[1]
    tailX = tail[0]
    tailY = tail[1]

    changeX = headX - tailX
    changeY = headY - tailY
    if abs(changeX) <= 1 and abs(changeY) <= 1:
        return (tailX, tailY)
    if changeY < 0:
        tailY -= 1
    if changeY > 0:
        tailY += 1
    if changeX < 0:
        tailX -= 1
    if changeX > 0:
        tailX += 1
    return (tailX, tailY)


while len(queue) > 0:
    # add the tails position
    tail = snake[-1]
    visited.append((tail[0], tail[1]))

    # move the head
    move = queue.pop(0)
    snake[0] = (snake[0][0]+move[0], snake[0][1]+move[1])

    # move the body of the snake
    for x in range(1,10):
        snake[x] = move_tail(snake[x-1], snake[x])
    
print(len(set(visited)))



    