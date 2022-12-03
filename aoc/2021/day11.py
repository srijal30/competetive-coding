from turtle import Turtle
from sqlalchemy import true


octos = [ [int(x) for x in row] for row in open("day11test.txt").read().splitlines()]

flashCount = 0
days = 0
#do it 100 times
while flashCount != 100:
    days += 1
    flashable = True
    step = True
    flashed = []
    #while one octo has flashed, continue iteration
    while flashable:
        flashable = False
        #for every row
        for row in range( len(octos) ):
            #for every col
            for col in range( len(octos[0]) ):
                #only increment once
                if step:
                    octos[row][col] += 1
                #if can flash, flash
                if octos[row][col] > 9 and [row, col] not in flashed:
                    flashable = True
                    flashCount += 1
                    flashed.append( [row, col] )
                    #do the flashing to adjacents
                    if row > 0:
                        octos[row-1][col] += 1
                    if row < 9:
                        octos[row+1][col] += 1
                    if col > 0:
                        octos[row][col-1] += 1
                    if col < 9:
                        octos[row][col+1] += 1
                    if row > 0 and col > 0:
                        octos[row-1][col-1] += 1
                    if row > 0 and col < 9:
                        octos[row-1][col+1] += 1
                    if row < 9 and col > 0:
                        octos[row+1][col-1] += 1
                    if row < 9 and col < 9:
                        octos[row+1][col+1] += 1
        #after you step once, then never allow it to happen again
        step = False
    #make all the ones that flashed back to 0
    for coord in flashed:
        octos[coord[0]][coord[1]] = 0
    if flashCount == 100:
        break
    else:
        flashCount = 0

print(days)



