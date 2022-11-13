import math
matrix = [ [int(y) for y in x] for x in open("day15test.txt").read().splitlines() ]

def update_tile( distance, tile ):
    return tile+distance - 9*math.floor((tile+distance)/9)

new_matrix = [ [] for x in range(500) ]
print( len(new_matrix) )

#make matrix good
for row_index in range( len(new_matrix) ):
    old_row = matrix[ row_index % 100 ]
    x = math.floor( row_index/100 )
    for y in range(5):
        new_matrix[row_index] += [ update_tile( y+x, i) for i in old_row ]


matrix = new_matrix

visited = []
queue = [] 
risk_map = {}

max_x = len(matrix)
max_y = len(matrix[0])

#setting up risk_map
for x in range(max_x):
    for y in range(max_y):
        risk_map[ (x, y) ] = math.inf
risk_map[ (0,0) ] = 0

queue.append( (0, 0) )

while len(queue) > 0:
    #if visited alr skip 
    coords = queue.pop(0)
    #print(coords)
    if coords in visited:
        continue
    #else mark as visited
    x,y = coords
    distance_here = risk_map[(x,y)]
    visited.append( coords )

    #find the valid directions to go to and add to queue
    #up
    if x-1 >= 0:
        #if the distance from here to next location is better... update
        if distance_here+matrix[x-1][y] < risk_map[ (x-1,y) ] and (x-1,y) not in visited:
            risk_map[ (x-1, y) ] = distance_here+matrix[x-1][y]
        queue.append( (x-1, y) )
    #down
    if x+1 < max_x:
        #if the distance from here to next location is better... update
        if distance_here+matrix[x+1][y] < risk_map[ (x+1,y) ] and (x+1,y) not in visited:
            risk_map[ (x+1, y) ] = distance_here+matrix[x+1][y]
        queue.append( (x+1, y) )
    #left
    if y-1 >= 0:
        #if the distance from here to next location is better... update
        if distance_here+matrix[x][y-1] < risk_map[ (x,y-1) ] and (x,y-1) not in visited:
            risk_map[ (x, y-1) ] = distance_here+matrix[x][y-1]
        queue.append( (x, y-1) )
    #right
    if y+1 < max_y:
        #if the distance from here to next location is better... update
        if distance_here+matrix[x][y+1] < risk_map[ (x,y+1) ] and (x,y+1) not in visited:
            risk_map[ (x, y+1) ] = distance_here+matrix[x][y+1]
        queue.append( (x, y+1) )

print( risk_map, "\n\n\n")
print( risk_map[ (max_x-1, max_y-1) ] )
