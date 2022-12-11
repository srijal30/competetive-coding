testerfile = open('5', 'r')
content = testerfile.read()
testerfile.close()
lines = content.splitlines()

# test
crates = {
    "1": ["F", "H", "M", "T", "V", "L", "D"],
    "2": [*"PNTCJGQH"],
    "3": [*"HPMDSR"],
    "4": [*"FVBL"],
    "5": [*"QLGHN"],
    "6": [*"PMRGDBW"],
    "7": [*"QLHCRNMG"],
    "8": [*"WLC"],
    "9": [*"TMZJQLDR"]
}

for line in lines:
    io = line.split(" from ")
    count = int(io[0].replace("move ", ""))
    start = io[1].split(" to ")[0]
    dest = io[1].split(" to ")[1]

    shipment = crates[start][0:count]
    crates[start] = crates[start][count:]
    crates[dest] = shipment + crates[dest] 

for key in crates:
    print(crates[key][0] if len(crates[key]) > 0 else "", end="")
print()
