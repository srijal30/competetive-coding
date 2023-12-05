
print(sum([__import__("functools").reduce(lambda x,y: x*y, [max([int(x) for x in __import__("re").findall(f"(:?\d+) {color}", game)]) for color in ["red","green","blue"]]) for game in open('2','r').read().splitlines()]))
