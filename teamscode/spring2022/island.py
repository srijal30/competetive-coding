io = input().split()

h = int( io[0] ) + 1
w = int( io[1] ) + 1

stuff = ""

rows = []

for i in range(h):
    io = input()
    things = io.split(" ")
    stuff += "".join(things)
    rows.append( things )

cols = [ [rows[col][row] for col in range(w)] for row in range(h) ]

current = stuff.count("B") * stuff.count("A")
print( "current:", current )


for row in range( len(rows) ):

    for col in range( len(rows[0] ) ):
        
        if rows[row][col] == "A":
            


print( current )
