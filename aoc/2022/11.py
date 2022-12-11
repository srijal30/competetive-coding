from typing import List, Callable

testerfile = open('11', 'r')
content = testerfile.read()
testerfile.close()
descriptions = [x.splitlines() for x in content.split("\n\n")]

COUNT = 8
MOD = 1

class Monkey():
    def __init__(self):
        self.items : List = []
        self.operation : Callable = None
        self.test : int = 0
        self.falseMonkey : Monkey = None
        self.trueMonkey : Monkey = None
        self.inspects = 0

    def give(self, item, monkey):
        self.items.remove(item)
        monkey.items.append(item)

    def execute(self):
        self.items = [self.operation(x)%MOD for x in self.items]
        self.inspects += len(self.items)
        for item in self.items.copy():
            if item % self.test == 0:
                self.give(item, self.trueMonkey)
            else:
                self.give(item, self.falseMonkey)


monkeys = [Monkey() for x in range(COUNT)]

for i in range(len(descriptions)):
    current = descriptions[i]
    # items
    monkeys[i].items = [int(x) for x in current[1].replace("  Starting items: ", "").split(", ")]
    # operator
    # gonna manually do this :)
    # test
    monkeys[i].test = int(current[3].replace("  Test: divisible by ",""))
    # throwing monkeys
    monkeys[i].trueMonkey = monkeys[int(current[4].replace("    If true: throw to monkey ",""))]
    monkeys[i].falseMonkey = monkeys[int(current[5].replace("    If false: throw to monkey ",""))]

for x in [monkey.test for monkey in monkeys]:
    MOD *= x

# ACTUAL
monkeys[0].operation = lambda x : x * 13
monkeys[1].operation = lambda x : x + 3
monkeys[2].operation = lambda x : x + 6
monkeys[3].operation = lambda x : x + 2
monkeys[4].operation = lambda x : x * x
monkeys[5].operation = lambda x : x + 4
monkeys[6].operation = lambda x : x * 7
monkeys[7].operation = lambda x : x + 7

# TEST
# monkeys[0].operation = lambda x : x * 19
# monkeys[1].operation = lambda x : x + 6
# monkeys[2].operation = lambda x : x * x
# monkeys[3].operation = lambda x : x + 3

for x in range(10000):
    print("round", x)
    for i in range(COUNT):
        monkeys[i].execute()

businesses = [x.inspects for x in monkeys]
businesses.sort()
print( businesses[-1] * businesses[-2])