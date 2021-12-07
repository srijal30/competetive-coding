import statistics
import fileinput

fil = ""
for line in fileinput.input("day7tests.txt"):
    fil += line

values = [int(x) for x in fil.split(",")]

fuel = []
minpos = min(values)
maxpos = max(values)
for value in values:
    fuel.append( [ (abs(value-x)*(abs(value-x)+1))/2 for x in range(minpos, maxpos+1)] )

summers = []
for col in range( len(fuel[0]) ):
    helper = []
    for row in range( len(fuel) ):
        helper.append( fuel[row][col] )
    
    summers.append( sum(helper) )
    

print( min(summers) )
