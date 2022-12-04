testerfile = open('4', 'r')
content = testerfile.read()
testerfile.close()
lines = content.splitlines()

ctr = 0
for line in lines:
    pairs = [[int(x) for x in y.split("-")] for y in line.split(",")]
    if pairs[0][0] >= pairs[1][0] and pairs[0][1] <= pairs[1][1] or pairs[0][1] >= pairs[1][0] and pairs[0][1] <= pairs[1][1]:
        ctr +=1
    elif pairs[1][0] >= pairs[0][0] and pairs[1][1] <= pairs[0][1] or pairs[1][1] >= pairs[0][0] and pairs[1][1] <= pairs[0][1]:
        ctr +=1
print(ctr)