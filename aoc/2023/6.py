time = 38677673
distance = 234102711571236

# time = 71530
# distance = 940200


low, high = [0, 0]
# find the lowest time
for i in range(time):
	if (time-i)*i > distance:
		low = i
		break
# find the greatest time
for i in range(low, time):
	if (time-i)*i <= distance:
		high = i
		break
print(high-low)
