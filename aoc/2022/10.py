testerfile = open('10', 'r')
content = testerfile.read()
testerfile.close()
lines = content.splitlines()

X = 1
cycle_queue = []
ctr = 0

render = ""

for line in lines:
    if line == "noop":
        cycle_queue.append(0)
    else:
        change = int(line.split(" ")[1])
        cycle_queue.append(0)
        cycle_queue.append(change)

while len(cycle_queue) > 0:
    # update the register

    # draw
    if ctr%40 in [X-1,X,X+1]:
        render += "#"
    else:
        render += "."
    
    # update counter
    X += cycle_queue.pop(0)
    ctr += 1

for index in range(len(render)):
    if index%40 == 0:
        print()
    print(render[index], end="")