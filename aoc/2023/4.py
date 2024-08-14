import re

content = open("4", 'r').read()
lines = content.splitlines()
card_counts = [1]*len(lines)

ans = 0
for i, card in enumerate(lines):
	nums = card.split(":")[1].split("|")
	winning = [int(x) for x in re.findall("\d+", nums[0])]
	mine = [int(x) for x in re.findall("\d+", nums[1])]
	cnt = 0
	for m in mine:
		if m in winning:
			cnt += 1
	for x in range(i+1, i+cnt+1):
		card_counts[x] += 1*card_counts[i]

print(sum(card_counts))
