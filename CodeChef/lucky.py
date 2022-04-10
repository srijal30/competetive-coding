times = int( input() )

for x in range(times):
    io = input().split(" ")
    n = int( io[0] )
    a = int( io[1] )
    b = int( io[2] )

    arr = [ int(i) for i in input().split(" ") ]

    bob = 0
    alice = 0
    both = 0

    for num in arr:
        if num == 0:
            pass
        if num%a:
            bob+=1
        if num%b:
            alice+=1
        if num%b and num%a:
            both += 1
    
    if both %2 == 0:
        pass
    else:
        alice -= 1
    
    if b > a:
            print("BOB")
    else:
            print("ALICE")


    


