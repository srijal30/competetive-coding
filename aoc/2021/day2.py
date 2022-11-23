import fileinput


values = []
for line in fileinput.input( files = "day2test.txt" ):
    lineArr = line.split()
    values.append( lineArr )

x = 0
y = 0
aim = 0

for command in values:
    if command[0] == "forward":
        x += int(command[1]) 
        y += aim* int(command[1])

    if command[0] == "down":
        aim += int(command[1])

    if command[0] == "up":
        aim -= int(command[1])

print( x*y)



