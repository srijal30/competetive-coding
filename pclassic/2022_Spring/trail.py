from re import M


times = int( input() )


def findWidestMountainRange( n, mts ):
    highest = 0

    for mIndex in range(n-2):
        
        current = mts[mIndex]
        
        distance = 1
        
        #this should stop when it gets to smaller 
        while mIndex + distance < n and current < mts[mIndex+distance] :
            current = mts[mIndex+distance]
            distance+=1
        
        if mIndex + distance < n:
            pass

        elif distance == 1 :
            pass
        
        else:
            #this goes to the next
            current = mts[mIndex+distance]
            distance += 1

            #this should stop when it hits a elevation higher
            while mIndex + distance < n and current > mts[mIndex+distance]:
                current = mts[mIndex+distance]
                distance+= 1

            highest = max( distance, highest )
    
    return highest

        


for x in range( times ):

    trailLength = int( input() )
    mountainRange = [ int(i) for i in input().split() ]

    print( findWidestMountainRange(trailLength, mountainRange) )
