testerfile = open('17', 'r')
shifts = testerfile.read()
testerfile.close()

board = [[]]*7

pieces = [
    [[*"..####."]],
    [[*"...#..."],["..#...."],["...#..."]],
    [[*"....#.."],[*"....#.."],["..#...."]],
    [[*"..#...."]*4],
    [[*"..##..."]*2]
]

pCnt = 0
while pCnt < 2200:
    curPiece = pieces[pCnt%5]
    

    pCnt += 1
    pass