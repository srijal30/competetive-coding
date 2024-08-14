import re

hands = {x.split(" ")[0]: int(x.split(" ")[1]) for x in open('7').read().splitlines()}
order = "J23456789TQKA"
types = [(5,), (4, 1), (3, 2), (3, 1, 1), (2, 2, 1), (2, 1, 1, 1), (1, 1, 1, 1, 1)]

def power(hand):
	power = 0
	t_set = list(reversed(sorted([hand.count(x) for x in list(set(hand))])))
	if 'J' in hand:
		j_index = len(t_set)-1-t_set[::-1].index(hand.count('J'))
		if j_index != 0:
			t_set[0] += t_set[j_index]
			t_set.pop(j_index)
		if j_index == 0 and len(t_set) > 1:
			t_set[0] += t_set[1]
			t_set.pop(1)
	t = len(types)-types.index(tuple(t_set))

	power += len(order)**5*t
	for i,h in enumerate(hand):
		power += len(order)**(4-i)*order.index(h)
	return power

keys = list(hands.keys())
keys.sort(key=power)

print(sum([hands[h]*(keys.index(h)+1) for h in keys]))

