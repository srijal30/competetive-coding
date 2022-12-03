testerfile = open('2', 'r')
content = testerfile.read()
testerfile.close()
lines = content.splitlines()

score = 0

yours = "XYZ"
theirs = "ABC"

for line in lines:
    io = line.split(" ")
    other = io[0]
    you = io[1]

    score += yours.index(you)*3
    if you == "X":
        if theirs.index(other) == 0:
            score += 3
        if theirs.index(other) == 1:
            score += 1
        if theirs.index(other) == 2:
            score += 2
    elif you == "Y":
        score += theirs.index(other) + 1
    else:
        if theirs.index(other) == 0:
            score += 2
        if theirs.index(other) == 1:
            score += 3
        if theirs.index(other) == 2:
            score += 1

print(score) 
    

    

