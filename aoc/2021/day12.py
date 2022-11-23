caves = {}

#go throught every line creating the cave graph
for line in open("day12test.txt").read().splitlines():
    orig = line.split("-")[0]
    dest = line.split("-")[1]
    if orig not in caves:
        caves[orig] = []
    if dest not in caves:
        caves[dest] = []
    caves[orig].append(dest)
    caves[dest].append(orig)

paths = 0

def explore(cave, explored, ful):
    #if we at end, then we found a path
    if cave == "end":
        return [["end"]]

    
    #check if current cave is small

    isSmall = cave.islower()

    #if the cave is small and has been explored alr
    if isSmall and cave in explored:
        if cave == "start":
          return None  
        #check if we have visited small cave twice
        elif not ful:
            ful = True
            pass
        #else we dont continue
        else:
            return None

    #add this cave to explored
    explored.append(cave)

    paths = []
    #find all the paths from children
    for branch in caves[cave]:
        result = explore(branch, explored.copy(), ful)
        #if there are paths
        if result != None:
            #add current cave to the path
            for x in result:
                x.append(cave)
                paths.append(x)            
    
    return paths

print( len(explore( "start", [], False )) )
