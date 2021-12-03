import fileinput


values = []

for line in fileinput.input("day3test.txt" ):
    values.append(line[:12])


values1 = values.copy()
values2 = values.copy()

values3 = values.copy()
values4 = values.copy()

indexTracker = 0

while len(values1) > 1:

    column = []
    for y in range( len(values1) ):
        column.append(values1[y][indexTracker])
    
    # if 0
    if column.count("0") > column.count("1"):
        for i in range( len(column) ):
            if len(values1) == 1:
                break
            if column[i] != "0":
                values1.remove( values2[i] )
    #if 1
    else:
        for i in range( len(column) ):
            if len(values) == 1:
                break
            if column[i] != "1":
                values1.remove( values2[i] )
    
    indexTracker +=1
    values2 = values1.copy()
    print( values2, indexTracker-1 )


indexTracker = 0
while len(values3) > 1:

    column = []
    for y in range( len(values3) ):
        column.append(values3[y][indexTracker])
    
    # if 0
    if column.count("0") > column.count("1"):
        for i in range( len(column) ):
            if len(values3) == 1:
                break
            if column[i] != "1":
                values3.remove( values4[i] )
    #if 1
    else:
        for i in range( len(column) ):
            if len(values) == 1:
                break
            if column[i] != "0":
                values3.remove( values4[i] )
    
    indexTracker +=1
    values4 = values3.copy()
        


print( int(values1[0], 2) * int(values3[0], 2) )

    
