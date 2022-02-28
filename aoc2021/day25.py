import os
ommiter = lambda x: ">" if ">" in x else "v" if "v" in x else "."

ground = [ [x for x in row] for row in open("day25tests.txt").read().splitlines() ]
rowLen = len(ground[0])
colLen = len(ground)


#next>
def nextR(col):
    col += 1
    return col if col < rowLen else 0

#nextv
def nextD(row):
    row += 1
    return row if row < colLen else 0

#resetter
def reset(ground):
    return [[ommiter(x) for x in row] for row in ground]

#for >
def easters(ground):
    for iRow in range( len(ground) ):
        for iCol in range( len( ground[iRow] ) ):
            if ground[iRow][iCol] == ">" and ground[iRow][ nextR(iCol) ] == ".":
                ground[iRow][iCol] = "."
                ground[iRow][ nextR(iCol) ]  = ".>"
    return reset(ground)

#for v
def southers(ground):
    for iRow in range( len(ground) ):
        for iCol in range( len( ground[iRow] ) ):
            if ground[iRow][iCol] == "v" and ground[ nextD(iRow)][ iCol ] == ".":
                ground[iRow][iCol] = "."
                ground[ nextD(iRow)][ iCol ] = ".v"
    return reset(ground)

#init
groundBefore = ground
ground = easters(ground)
ground = southers(ground)
counter = 0

def printer(thing):
    for row in thing:
        print(row)

#continue
while groundBefore != ground:
    groundBefore = ground
    ground = easters(ground)
    ground = southers(ground)
    counter += 1
    print(counter)
#print result
print( counter )