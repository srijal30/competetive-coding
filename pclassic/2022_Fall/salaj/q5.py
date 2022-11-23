def adj(start, dest):
    if start == "A" or start =="C":
        return dest == "B" or dest == "D"
    else:
        return dest =="A" or dest =="C"

def timefor(n, k, order, duration, person):
    start = person[0]
    end = person[1]
    time = int(person[2])

    stff = "".join([order[x]*duration[x] for x in range(n)])
    adjfound = adj(start, end)

    for i in range(time, len(stff)):
        adjfound = adjfound or adj(start, stff[i])
        if adjfound and stff[i] == end:
            return i-time
    return -1


# Implement the following function
def evacuate(n, k, order, duration, sfx):
    res = []
    for person in sfx:
        res.append(timefor(n, k, order, duration, person))
    return res


tests = int(input().strip()) # Number of test cases
for test in range(tests):
    line = input().strip().split(' ')
    n = int(line[0])
    k = int(line[1])
    order = input().strip().split(' ') # List of which portals turn on in order
    duration = input().strip().split(' ') # List of times when portals are on for
    duration = [int(x) for x in duration]
    sfx = [] # List of triplets (start_portal, destination_portal, arrival_time)
    for _ in range(k):
        sfx.append(input().strip().split(' '))
    ret_arr = evacuate(n, k, order, duration, sfx)
    ret_arr = [str(x) for x in ret_arr]
    print('\n'.join(ret_arr))
