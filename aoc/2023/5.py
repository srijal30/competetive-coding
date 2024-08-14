import re

content = open('5', 'r').read()
# get ranges of the seeds
seeds = [(int(x.split(" ")[0]), int(x.split(" ")[0])+int(x.split(" ")[1])-1) for x in re.findall("\d+ \d+", content[0:content.index("\n")])]
# print(seeds)
# for each conversion
for mat in content.split("\n\n")[1::]:
	print("\n=============================\nNEW MAT")
	# create the list of mapping rules
	convert = []
	for line in mat.splitlines()[1::]:
		nums = [int(x) for x in line.split(" ")]
		convert.append(nums)
	
	# convert the ranges
	converted_seeds = []
	while len(seeds) > 0:
#		print("\nseeds", seeds)
		cs = seeds.pop(0)
		cnved = False
#		print("cs:", cs)
		# check to see what rules apply
		for cnv in convert:
			dest, src, l = cnv
#			print("cnv:", cnv)
			# check if cur seed range is in range
			if cs[0] < src+l and cs[1] >= src:
				cnved = True
#				print("applying")
				# convert and split if necassary
				new_seed_min = max(cs[0], src) + (dest-src)
				new_seed_max = min(cs[1], src+l-1) + (dest-src)
				converted_seeds.append((new_seed_min, new_seed_max))
				if cs[0] < src:
					seeds.append((cs[0], src-1))
				if cs[1] >= src+l:
					seeds.append((src+l, cs[1]))
		if not cnved:
			converted_seeds.append(cs)
	seeds = converted_seeds

#print(seeds)
# find the lowest number in all of the ranges
print(min([x[0] for x in seeds]))


