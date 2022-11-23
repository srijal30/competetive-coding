# Implement the following function
# returns the amount of steps
import sys
sys.setrecursionlimit(2000000)
def solution(n, chars, counts, curindex, charstyped, copiedchar, copiedcount, copiedindex, memo):
    # print(curindex, charstyped, "'"+copiedchar+"'", copiedcount)
    others = []
    
    # update the vars judging by charstyped
    if charstyped == counts[curindex]:
        charstyped = 0
        curindex+=1
    # if in the memo
    if (curindex, charstyped, copiedchar, copiedcount, copiedindex) in memo:
        return memo[(curindex, charstyped, copiedchar, copiedcount, copiedindex)]
    # if we r done
    if n == curindex:
        return 0

    # copy previous substring
    # we are changing copied char and copied count
    if copiedchar == '' :
        newchar = chars[curindex]
        newcount = counts[curindex]
        newindex = curindex
        if charstyped == 0 and curindex > 0:
            newchar = chars[curindex-1]
            newcount = counts[curindex-1]
            newindex = curindex-1
        others.append(solution(n, chars, counts, curindex, charstyped, newchar, newcount, newindex, memo)+1)

    # type first letter
    # we are chaning the chars typed
    others.append(solution(n, chars, counts, curindex, charstyped+1, copiedchar, copiedcount, copiedindex, memo)+1)

    # paste the substring
    # we are changing the chars typed
    if chars[curindex] == copiedchar and copiedcount + charstyped <= counts[curindex]:
        others.append(solution(n, chars, counts, curindex, copiedcount+charstyped, copiedchar, copiedcount, copiedindex, memo)+1)
    memo[(curindex, charstyped, copiedchar, copiedcount, copiedindex)]  = min(others)
    return memo[(curindex, charstyped, copiedchar, copiedcount, copiedindex)]


def molasses(n, c, l):
    return solution(n, c, l, 0, 0, '', 0, 0, {})


tests = int(input().strip()) # Number of test cases
for test in range(tests):
    n = int(input().strip())
    c = input().strip().split(' ')
    l = input().strip().split(' ')
    l = [int(x) for x in l]
    print(molasses(n, c, l))
