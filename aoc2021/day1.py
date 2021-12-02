import fileinput

count = 0
values = []


for line in fileinput.input(files = "day1test.txt" ):
    values.append( int(line) )

for x in range( len(values)-3 ):
    window = sum( values[x:x+3])
    nextWindow = sum( values[x+1:x+4])

    if nextWindow > window:
        count += 1


print(count)