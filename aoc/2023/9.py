content = open(0).read()
lines = content.splitlines()

ans1 = 0

def extra(nums):
    if not all([x == 0 for x in nums]):
        diffs = [nums[i] - nums[i-1] for i in range(1, len(nums))]
        return extra(diffs) + diffs[-1]
    return 0

for l in lines:
    nums = list(reversed([int(x) for x in l.split()]))
    ans1 += nums[-1] + extra(nums)

print(ans1)
