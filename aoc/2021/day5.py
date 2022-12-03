import fileinput

values = []
for line in fileinput.input("day5tests.txt"):
    sepLine = line.split(" ")
    sepLine[2] = sepLine[2][:-1]
    start = [int(x) for x in sepLine[0].split(",")]
    end = [int(x) for x in sepLine[2].split(",")]
    currentLine = []
    for x in start:
        currentLine.append(x)
    for x in end:
        currentLine.append(x)
    values.append(currentLine)

board = [ [0 for x in range(1000)] for y in range(1000) ] #change back

for value in values:
    #col same
    if value[0] == value[2]:
        rang = abs(value[3]-value[1] )
        small = min( value[3], value[1] )
        for row in range( small, small+rang+1):
            board[ row ][ value[0] ] += 1
    #row same
    elif value[1] == value[3]:
        rang = abs(value[0]-value[2])
        small = min( value[0], value[2] )

        for col in range( small, small+rang+1):
            board[ value[1] ][ col ] += 1
    
    elif abs(value[0] - value[2]) == abs(value[1]-value[3]):
        rang = abs(value[0]-value[2] )
        xStart = 0
        yStart = 0
        yInc = 0
        if value[0] <= value[2]:
            xStart = value[0]
            yStart = value[1]
            yInc = (value[3] - value[1])/rang
        else:
            xStart = value[2]
            yStart = value[3]
            yInc = (value[1] - value[3])/rang
        for ran in range(rang+1):
            board[ yStart ][ xStart ] += 1
            xStart += 1
            yStart += int(yInc)

        
count = 0
for row in board:
    for column in row:
        if column > 1:
            count +=1

print(count) 
