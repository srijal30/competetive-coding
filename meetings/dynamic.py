memo = {}
def fib( n ):
    if n in memo:
        return memo[n]
    if n == 0:
        return 1
    if n == 1:
        return 1
    
    memo[n] = fib(n-1) + fib(n-2)
    return memo[n]


print( fib( 1 ) )
print( fib( 2 ) )
print( fib( 6 ) )
print( fib( 53 ) )
