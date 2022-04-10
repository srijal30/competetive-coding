content = open("day8test.txt", "r").read().splitlines()

count = 0

def get(my_dict, val):
    for key, value in my_dict.items():
         if val == value:
             return key
 
    raise Exception("not a value in dict")


def find_dif(a, b):
    result = ""
    for x in a:
        if x not in b:
            result += x
    for x in b:
        if x not in a:
            result += x
    return result

def find_sim(a, b):
    bigger = max( a, b, key=lambda x: len(x) )
    smaller = min(a, b, key=lambda x: len(x))
    result = ""
    for x in bigger:
        if x in smaller:
            result += x
    return result

def combine(a, b):
    return "".join(sorted(list(set(a + b))))

def create_map( inputs ):
    the_map = {}
    missing2 = []
    missing1 = []
    #get the simples
    for i in inputs:
        #for 1
        if len(i) == 2:
            the_map[i] = '1'
        #for 4
        if len(i) == 4:
            the_map[i] = '4'
        #for 7
        if len(i) == 3:
            the_map[i] = '7'
        #for 8
        if len(i) == 7:
            the_map[i] = '8'
        #if missing 1
        if len(i) == 6:
            missing1.append(i)
        #if missing 2
        if len(i) == 5:
            missing2.append(i)

    #to get 6
    tmp = find_dif(get(the_map, '7'), get(the_map, '8'))
    for x in missing1:
        if len( find_sim(x, tmp) ) == 4:
            the_map[x] = '6'
            missing1.remove(x)
    #to get 9 and 0
    if find_dif( get(the_map, '8'), missing1[0] ) in get(the_map, '4'):
        the_map[ missing1[0] ] = '0'
        the_map[ missing1[1] ] = '9'
    else:
        the_map[ missing1[1] ] = '0'
        the_map[ missing1[0] ] = '9'
    #to get 2
    tmp = find_dif( get(the_map, '8'), get(the_map, '9') )
    for x in missing2:
        if tmp in x:
            the_map[x] = '2'
            missing2.remove(x)
    #get 3 and 5
    tmp = find_dif( get(the_map, '6'), get(the_map, '8') )
    if tmp in missing2[0]:
        the_map[ missing2[0] ] = '3'
        the_map[ missing2[1] ] = '5'
    else:
        the_map[ missing2[1] ] = '3'
        the_map[ missing2[0] ] = '5'

    return the_map


s = 0
for line in content:
    #the input specifically
    inputs = [''.join(sorted(x)) for x in line.split("|")[0].split() ]
    #the output specifically
    outputs = [''.join(sorted(x)) for x in  line.split("|")[1].split() ]

    the_map = create_map( inputs )

    current = int( ''.join( [ the_map[x] for x in outputs])   )
    print(current)
    s+=current
print(s)