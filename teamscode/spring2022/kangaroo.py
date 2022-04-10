#reading lines

io = int( input() )


l = []

for i in range(io):

    times = int( input() )
    inst = input()

    ytotal = 0
    xtotal = 0

    currentx = 0
    currenty = 0
    
    for x in inst:
        if x == "D":
            currenty-=1
        if x == "U":
            currenty+=1
        if x == "L":
            currentx-=1
        if x == "R":
            currentx+=1

        ytotal = max( abs(currenty), ytotal)
        xtotal = max( abs(currentx), xtotal)

    l.append( (xtotal+1,ytotal+1) )

for x in l:
    print( x )

