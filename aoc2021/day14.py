polymer = "FPNFCVSNNFSFHHOCNBOB"

rules = { x.split(" -> ")[0]: x.split(" -> ")[1] for x in open("day14test.txt").read().splitlines() }

key = {'O':0, 'H':0, 'V':0, 'K':0, 'P':0, 'B':0, 'N':0, 'S':0, 'F':0, 'C':0}

#better solution
def findCount( pair, iterations, memo={} ):
    result = key.copy()

    if (pair, iterations) in memo:
        return memo[ (pair, iterations) ]

    #if cant make child, then return
    if iterations == 0:
        return result

    #if you can, then add child to result
    child = rules[pair]
    result[child] += 1

    #findCount of children parent combination
    left = findCount( pair[0]+child, iterations-1, memo )
    right = findCount( child+pair[1], iterations-1, memo )

    #combine the results
    for x in key:
        result[x] += left[x]
        result[x] += right[x]

    memo[ (pair, iterations) ] = result

    return result


result = key.copy()

for index in range( len(polymer)-1 ):
    temp = findCount( polymer[index]+polymer[index+1], 40)
    for x in key:
        result[x] += temp[x]

test = []
for x in result:
    test.append( result[x] )

test = [ x for x in test if x!=0]


print( max(test) - min(test) + 1) #plus 1 cuz didnt account for last element


#bad solution
exit()
for x in range(40):
    print(x)
    newpoly = ""
    for index in range( len(polymer)-1 ):
        newpoly += polymer[index]
        newpoly += rules[  polymer[index]+polymer[index+1]   ]
    newpoly += polymer[-1]
    polymer = newpoly
allchars = list( set(newpoly)  )
allchars = [ polymer.count(x) for x in allchars ]
print( max(allchars)-min(allchars) )