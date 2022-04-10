io = input().split(" ")

times = int( io[0] )
k = int( io[1] )


def solve(u, s, steps):
    if u == s * k:
        return steps
    
    if u%k != 0:
        lower = int( u/k*k+1 )
        higher = int( (u+k)/k*k+1 )

        if abs(u-lower) < abs(u-higher):
            return solve( lower, s, steps+abs(u-lower))
        else:
            return solve( higher, s, steps+abs(u-higher) )

    if u > s*k:
        return solve( u, s+1, steps+1)
    else:
        return solve( u, s-1, steps+1)

sum = 0
for i in range(times):
    io = input().split(" ")
    sum += solve( int(io[0]), int(io[1]), 0)

print( sum )


    
