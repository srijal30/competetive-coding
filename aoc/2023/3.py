import re
import functools
content = open('3', 'r').read()
n = content.index('\n')
print(n)
content = "".join(content.splitlines())
ans = 0
numbers = [0]*len(content)
around = [-1, 1, -n, n, -n-1, -n+1, n+1, n-1]

# find numbers
for num in re.finditer("\d+", content):
	s = num.start()
	e = num.end()
	n = int(content[s:e])
	numbers[s:e] = [n]*(e-s)

# match symbol to number
for sym in re.finditer("\*", content):
	adj = [y for y in [numbers[sym.start()+x] for x in around] if y != 0]
	if len(set(adj)) == 2:
		ans += functools.reduce(lambda x,y: x*y, list(set(adj)))

print(ans)
	
