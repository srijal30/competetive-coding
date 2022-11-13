#how many seats
seats = int( input() )
#where each person goes
directions = [ int(x) - 1 for x in input().split(" ") ]

unvisited = [x for x in range(seats)]

#for every seat
for seat in range(seats):
    visited = []
    next = seat

    #keep on going until we hit a repeat
    #post condition, next is something we alr visited
    while next not in visited:
        visited.append(next)
        next = directions[next]


    #then continue to keep on going until all things in cycle removed from unvisited
    while next in unvisited:
        unvisited.remove(next)
        next = directions[next]

print( seats - len(unvisited) )