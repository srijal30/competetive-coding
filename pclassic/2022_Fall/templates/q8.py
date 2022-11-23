# Implement the following function
def molasses(n, c, l):
    pass


tests = int(input().strip()) # Number of test cases
for test in range(tests):
    n = int(input().strip())
    c = input().strip().split(' ')
    l = input().strip().split(' ')
    l = [int(x) for x in l]
    print(molasses(n, c, l))
