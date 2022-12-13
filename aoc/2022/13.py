testerfile = open('13', 'r')
content = testerfile.read()
testerfile.close()

items = [eval(x) for x in content.splitlines()] + [[[2]], [[6]]]

# 1 if right order
# -1 if not right order
# 0 if we still need to keep looking
def comp(left, right):
    for i in range(len(left)):
        # run out
        if i >= len(right):
            return -1
        # integer cases
        if type(left[i]) == int and type(right[i]) == int:
            if left[i] < right[i]:
                return 1
            if left[i] > right[i]:
                return -1
            else:
                continue
        # list case
        if type(left[i]) != list:
            left[i] = [left[i]]
        if type(right[i]) != list:
            right[i] = [right[i]]
        val = comp(left[i].copy(), right[i].copy())
        if val == 0:
            continue
        return val
    # find out if draw or ran out
    if len(right) > len(left):
        return 1
    else:
        return 0

import functools
key = functools.cmp_to_key(comp)
items.sort(key=key)
items = list(reversed(items))
print( (items.index([[6]]) + 1) * (items.index([[2]]) + 1) )
