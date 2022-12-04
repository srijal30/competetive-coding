testerfile = open('3', 'r')
content = testerfile.read()
testerfile.close()
lines = content.splitlines()

lower = "abcdefghijklmnopqrstuvwxyz"

total = 0
for index in range(0, len(lines), 3):
    one = lines[index]
    two = lines[index+1]
    three = lines[index+2]

    for x in one:
        if x in two and x in three:
            total += lower.index(x.lower()) + 1
            if x.isupper():
                total += 26 
            break

print(total)