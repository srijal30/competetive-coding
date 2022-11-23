n = int(input())

def comb(n):
    arr = [2**i for i in range(6)]
    if n <= 6:
        return arr[n-1]
    for i in range(n-6):
        tmp = sum(arr)
        arr.pop(0)
        arr.append(tmp)
    return arr[5]

print(comb(n) % (10**9+7))

