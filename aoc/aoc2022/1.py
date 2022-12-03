content = open('1', 'r').read()

elves = [sum([int(x) for x in y.split("\n")]) for y in content.split("\n\n")]
elves.sort()
print(sum(elves[-3:]))
