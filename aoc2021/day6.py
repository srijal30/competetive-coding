import fileinput

values = []
for line in fileinput.input("day6tests.txt"):
    values = [ int(x) for x in line.split(",") ]


print(values)

tempValues = [
values.count(0),
values.count(1),
values.count(2),
values.count(3),
values.count(4),
values.count(5),
values.count(6),
values.count(7),
values.count(8)
]

values = tempValues.copy()

for day in range(256):

    values[0] = tempValues[1]
    values[1] = tempValues[2]
    values[2] = tempValues[3]
    values[3] = tempValues[4]
    values[4] = tempValues[5]
    values[5] = tempValues[6]
    values[6] = tempValues[7] + tempValues[0]
    values[7] = tempValues[8]
    values[8] = tempValues[0]
    
    tempValues = values.copy()


print( sum(values) )