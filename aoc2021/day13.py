content = open("day13test.txt").read().splitlines()

#I REVERSED X AND Y TO MAKE MORE SENSE

#get the coords
coords = []
for x in range(881):
    xy = content[x].split(",")
    coords.append( [int(xy[1]), int(xy[0])] )

#get the folds
folds = []
for x in range(882, 894):
    if "x" in content[x]:
        folds.append( ["y", int(content[x].split("=")[1])] )
    if "y" in content[x]:
        folds.append( ["x", int(content[x].split("=")[1])] )

print( len(coords) )
for fold in folds:
    newcoords = []
    #if folding up
    if fold[0] == "x":
        for coord in coords:
            if coord[0] > fold[1]:
                pros = [ 2*fold[1]-coord[0] , coord[1] ]
                if pros not in coords:
                    newcoords.append( pros )
            else:
                newcoords.append( coord )

    #if folding left
    if fold[0] == "y":
        for coord in coords:
            if coord[1] > fold[1]:
                pros = [ coord[0], 2*fold[1]-coord[1] ]
                if pros not in coords:
                    newcoords.append( pros )
            else:
                newcoords.append( coord )
    coords = newcoords

print( len(coords) )

#find the max x
height = max( coords , key=lambda x: x[0] )[0]
length  = max( coords , key=lambda x: x[1] )[1]

#set up the initial paper
paper = [ ["." for col in range(length+1)] for row in range(height+1) ]
for coord in coords:
    paper[ coord[0] ][ coord[1] ] = "#"

for row in paper:
    for col in row:
        print(col, end="")
    print()