#parse the file into lines
values = [x for x in open("day8tests.txt").read().splitlines() ]


#parse each line; creating a list of each digit in output (in alphabetical order)
outputs = [ ["".join(sorted(y)) for y in x.split(" | ")[1].split(" ")] for x in values]

#find out each num
def findNum( scramble ):
    references = [ "" for x in range( 10 ) ]
    
    counts = [len(x) for x in scramble]
	print(counts)  
	
	for seq in scramble:
    	if seq in references:
            continue
                
        elif length == 2:
            references[1] = seq

        elif length == 3:
            references[7] = seq

        elif length == 4:
            references[4] = seq

        elif length == 5:
            pass
            #2
            #3
            #5

        elif length == 6:
            pass
            #0
            #6
            #9

        elif length == 7:
            references[8] = seq

    

    #find what combo for each number
    number = "" 

    for digit in scramble:
        #add the digit to number
        number += str( references.index( digit ) )


    #return the int form of the number
    return int(number)


#find the sum of all the numbers
adding = 0
for output in outputs:
    sum += findNum( output )

#print(adding)
