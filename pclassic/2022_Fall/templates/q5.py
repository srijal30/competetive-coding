# Implement the following function
def evacuate(n, k, order, duration, sfx):
    pass


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
