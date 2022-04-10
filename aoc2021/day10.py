
lines = open( "day10test.txt", "r").readlines()

point = \
{
    "(": 1,
    "[": 2,
    "{": 3,
    "<": 4,
}

scores = []

opening = "([{<"
closing = ")]}>"

index = 0
for line in lines:
    stack = []
    ignore = False
    #check every char in line
    for char in line:
        #if char is opening then add it to stack
        if char in opening:
            stack.append(char)
            continue
        #if it a closing, then...
        elif char in closing:
            popped = stack.pop()
            #if it is a match then continue parsing the line
            if opening.index( popped ) == closing.index(char):
                continue
            #if it is not a match then stop parsing the line
            else:
                ignore = True
                break
        #if not closing or opening, then probably a newline so just continue
        else:
            continue

    #at the end, line might be incomplete, check all the parens that still need to be matched
    #check if we are ignoring this line
    if ignore:
        continue
    #else calculate the score
    score = 0
    while( len(stack) > 0 ):
        popped = stack.pop()
        score *= 5
        score += point[ popped ]
    
    scores.append( score )
    index += 1

scores = sorted(scores)

print( scores[int( len(scores)/2)] )

