content = open("15", 'r').read()

# maxval = 4000000
maxval = 20

rows = {} # there will be a "domain" in each row

def tuning_frequency(x, y):
    return x*4000000+y

def get_distance(x1, y1, x2, y2):
    return abs(x1-x2) + abs(y1-y2)

# row is y val -- i mixed it up
def update_domain(irow, left, right):
    # update the bounds
    left = max(0, left)
    right = min(maxval-1, right)
    # add new list if does not exist
    if irow not in rows:
        rows[irow] = [(0, maxval)]
    cur = rows[irow]
    # check for edge cases
    if len(cur) <= 0:
        return
    if right < cur[0][0] or left > cur[-1][1]:
        return

    # build the new domain
    leftpart = []
    middlepart = []
    rightpart = []

    # find left index
    li = 0
    if left <= cur[0][0]:
        # leftpart stays none
        li = -1
    else:
        while left > cur[li][1]:
            li += 1
        leftpart = cur[0:li]

    # find right index
    ri = len(cur)-1
    if right >= cur[-1][1]:
        #right part stays the same 
        ri = -1
    else:
        while right < cur[ri][0]:
            ri -= 1
        rightpart = cur[ri+1:-1]
    
    if ri == -1 and li == -1:
        middlepart = []
    elif li == -1:
        middlepart = [(right+1, cur[ri][1])]
    elif ri == -1:
        middlepart = [(cur[li][0], left-1)]
    elif ri == li:
        middlepart = [(cur[li][0], left-1), (right+1, cur[ri][1])]
    
    rows[irow] = leftpart + middlepart + rightpart
    # DEBUG
    print(li, ri)
    print("left part", cur[0:li])
    print("middlepart part", middlepart)
    print("right part", cur[ri+1:-1])
    print()

update_domain(0, 5, 10)
update_domain(0, 7, 8)
update_domain(0, 2, 9)
exit()

ctr = 0
for l in content.splitlines():
        # print(ctr); ctr+=1
        # sensor
        x1 = l.split("x=")[1].split(',')[0]
        x2 = l.split("x=")[2].split(',')[0]
        # beacon
        y1 = l.split("y=")[1].split(':')[0]
        y2 = l.split("y=")[2].split(':')[0]
        x1, x2, y1, y2 = list(map(int, [x1,x2,y1,y2]))
        # get the dist
        dist = get_distance(x1, y1, x2, y2)
        for i in range(y1-dist, y1+dist+1):
                sym = dist-abs(y1-i)
                if x1 == 8 and y1 == 7:
                    print(sym)
                update_domain(i, x1-sym, x1+sym)
