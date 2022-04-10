import numpy as np

times = int( input() )

for x in range( times ):
    
    dunes =  [ [int(s) for s in input().split()] for i in range(4) ]

    inst = input().split()

    for direction in inst:
        
        if direction == "S":
            #for each row starting from the 2nd one
            for x in range( 1, 4):
                #add the row above
                dunes[x] = [ dunesCopy[x][i] + dunesCopy[x-1][i] for i in range(4)]

    print( dunes )
