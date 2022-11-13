io = input().split(" ")

init_d = int( io[1] )
times = int( io[0] )

#old frames (store old universe)
old_frames = []

#every position for every second
frames = [ init_d ]
latest_query = 0

def wait( time ):
    #create new frames
    for x in range(time):
        if frames[-1] > 0:
            frames.append( frames[-1] - 1 )
        else:
            frames.append( frames[-1] )

def teleport( d ):
    frames[-1] += d

def rewind( time ):
    global old_frames
    global frames
    old_frames = frames.copy() 
    frames = frames[0:len(frames)-time]

def revert():
    global frames
    global old_frames
    temp = old_frames
    old_frames = frames
    frames = temp

def query():
    global latest_query 
    latest_query = min(frames)
    print( latest_query )

for x in range(times):
    
    io = input().split(" ")

    x = int(io[0]) ^ latest_query
    y = int(io[1]) ^ latest_query

    if x == 0:
        query()
    elif x == 1:
        wait(y)
    elif x == 2:
        teleport(y)
    elif x == 3:
        rewind(y)
    elif x == 4:
        revert()
    else:
        Exception("What the hell happened")



