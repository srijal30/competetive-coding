def fib( n, dic={} ):

    if n in dic:
        return dic[n]
    if n < 2:
        dic[n] = 1 
    else:
        dic[n] = fib(n-1, dic) + fib(n-2, dic)
    return dic[n]



print( fib(1) )
print( fib(2) )
print( fib(3) )
print( fib(4) )
print( fib(5) )
print( fib(6) )
print( fib(7) )
print( fib(8) )
print( fib(200) )

