import math


input()

trans = [ "life", "heaven", "earth"]

first = [ trans.index(x) for x in input().split(" ")]
second = [ trans.index(x) for x in input().split(" ")]


t1 = len(first)-1
t2 = len(second)-1

result = []
carry = 0

while t1 >= 0 and t2 >= 0:
    
    if t1 < 0:
        result.append( second[t2] )
        t2 -= 1

    elif t2 < 0:
        result.append( first[t1] )
        t1 -= 1

    else:

        result.append( (first[t1] + second[t2] + carry) % 3 )
        

        carry = math.floor( (first[t1] + second[t2])/3 )
        
        t1 -= 1
        t2 -= 1

        if t1 < 0 and t2 < 0:
            if carry > 0:
                result.append(carry)
        
            

result = reversed(result)
print( " ".join( [trans[x] for x in result] ) )

