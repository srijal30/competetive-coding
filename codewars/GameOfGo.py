class Go:
    ###Instance Vars
    
    #Needed for KATA
    board = []
    turn = "black"
    size = {"height": 0, "width": 0}

    #Constructor
    def __init__(self, *args):
        #with 2 args
        if len(args) > 1:
            if args[0] > 25 or args[1] > 25:
                raise ValueError("Board is too big!")
            self.size["height"] = args[0]
            self.size["width"] = args[1]
            self.board = [ ["." for col in range(args[1])] for row in range(args[0]) ]
        #with 1 arg
        else:
            if args[0] > 25:
                raise ValueError("Board is too big!")
            self.size["height"] = args[0]
            self.size["width"] = args[0]
            self.board = [ ["." for col in range(args[0])] for row in range(args[0]) ]

    ###Methods
    
    #to pass a turn
    def pass_turn(self):
        self.turn = "white" if self.turn == "black" else "black"
        #might have to add functionality to make this count as a turn
    
    #reset the board
    def reset(self):
        self.turn = "black"
        self.board = [ ["." for col in range(self.size["width"])] for row in range(self.size["height"]) ]

    #convert position to a coord
    def get_coords(self, position):
        #check if height out of bounds
        if int(position[:-1]) > self.size["height"]:
            raise ValueError("Height out of bounds!")
            return [self.size["height"]+1, self.size["width"]+1 ] 
        row = ord( position[-1] ) - 65 #might have to make lowercase
        #check if row out of bounds
        if row >= self.size["width"]:
            raise ValueError("Width is out of bounds!")
        col = self.size["height"] + int( position[:-1]) 
        col %= self.size["height"]
        return [row, col-1]

    #get position
    def get_position(self, position):
        coords = self.get_coords(position)
        return self.board[ coords[0] ][ coords[1] ]

    #make a move
    def move(self, *positions):
        for position in positions:
            #check if empty
            if self.get_position(position) !=  ".":
                raise ValueError("There is already a piece there!")
            #put o or x depending oh whose turn
            coords = self.get_coords(position)
            piece = "o" if self.turn == "white" else "x"
            self.board[ coords[0] ][ coords[1] ] = piece
            #change turn
            self.turn = "black" if self.turn == "white" else "white"





#constructor with 1 arg test
#testBoard = Go(5)
#print( testBoard.board, "\n")
#print( testBoard.size )
#badBoard = Go(26)

#constructor with 2 arg test
testBoard = Go(5, 4)
#print(testBoard.board)
#print( testBoard.size )
#badBoard = Go(12, 26)
#badBoard = Go(27, 25)

#turn test
#print( testBoard.turn )
#testBoard.pass_turn()
#print( testBoard.turn)

#move test
#testBoard.move("1A")
#testBoard.move("1B")
#testBoard.move("1C")
#testBoard.move("1D")
#testBoard.move("1A", "1B", "1C", "1D")
#print( testBoard.board)

#reset test
#testBoard.reset()
#print( testBoard.board )

#invalid move test
#print( testBoard.move("1A") )
#print( testBoard.move("1A") )
#print( testBoard.move("1G") )
#print( testBoard.move("6B") )

#get_position test
#print( testBoard.get_position("1A") )
#print( testBoard.get_position("1B") )
#print( testBoard.get_position("1C") )
#print( testBoard.get_position("1D") )

#handicap test

