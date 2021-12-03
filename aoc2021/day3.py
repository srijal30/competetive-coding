import fileinput


values = []

for line in fileinput.input("day3test.txt" ):
    values.append(line[:12])

def findMin( arr , bit):
    column = [ arr[x][bit] for x in range(arr) ]
    if column.count("1") > column.count("0")
        return "1"
    return "0"
    

def findMax( arr , bit):
    column = [ arr[x][bit] for x in range(arr) ]
    if column.count("0") > column.count("1")
        return "0"
    return "1"

values1 = values.copy()
values2 = values.copy()

indexTracker = 0
while len(values1) > 1:
    
    keepSafe = findMax( values1, indexTracker )
    values1 = [ values1[x] for x in range(len(values1)) if values1[x][indexTracker] == keepSafe]
    indexTracker += 1

indexTracker = 0
while len(values2) > 1:
    
    keepSafe = findMin( values2, indexTracker )
    values2 = [ values1[x] for x in range(len(values1)) if values1[x][indexTracker] == keepSafe]
    indexTracker += 1        


print( int(values1[0], 2) * int(values2[0], 2) )

    
