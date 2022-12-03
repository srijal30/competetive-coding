import fileinput

#turn input into string to make it easier to parse
fil = ""
for line in fileinput.input("day4tests.txt"): #need to change back
    fil += line
fil = fil.split("\n", 1)

#find the sequence
sequence = [int(x) for x in fil[0].split(",") ]

#fill up the boards
boards = [ [] for x in range(100) ] #need to change this back
boardInput = fil[1].split("\n")

for board in boards:
    currentLine = boardInput.pop(0)

    while currentLine != "":
        board.append( [ int(num) for num in currentLine.split() ] )
        if boardInput == []:
            break
        currentLine = boardInput.pop(0)

#helper method
def mark( seq ):
    winningBoards = []
    #Loop through each board
    for boardNumber in range( len(boards) ):
        #Loop through each row
        for rowNumber in range( len(boards[boardNumber]) ):
            #Loop through each column
            for colNum in range( len(boards[boardNumber][rowNumber]) ):
                #Check if current spot num is == to seq
                if boards[boardNumber][rowNumber][colNum] == seq:
                    boards[boardNumber][rowNumber][colNum] = "0"
                    #If it is equal change it to "0" and check if there is winning position
                    #Check the row
                    if boards[boardNumber][rowNumber] == ["0", "0", "0", "0", "0"]:
                        winningBoards.append(boardNumber)
                        continue
                    #Check the column
                    #print( boards[boardNumber][x][colNum] for x in range(5) )
                    
                    elif [boards[boardNumber][x][colNum] for x in range(5)] == ["0", "0", "0", "0", "0"]:
                        winningBoards.append(boardNumber)
                    
    return winningBoards


result = 0
currentSeq = 0

tempBoard = boards.copy()

for seq in sequence:
    winningBoards = mark(seq)
    if winningBoards == []:
        continue

    for winningBoard in winningBoards:
        current = boards[winningBoard]
        tempBoard.remove( current) 
        if tempBoard == []:
            result = current
            currentSeq = seq
            break
    
    boards = tempBoard.copy()

print(sequence)
print(currentSeq)

adding = 0
for row in result:
    adding += sum( [int(x) for x in row])

print(adding)


