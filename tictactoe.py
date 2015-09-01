'''
Tic Tac Toe

1. 2 player game
2. Create game board, 3x3 with dashes in between

    0|1|2
    3|4|5
    6|7|8

3. Player can select which square they want to play
4. Check to make sure that square hasn't been played
5. Use a list to check [tl, tm, tr, ml, mm, mr, bl, bm, br]
6. Need to check for winner after each move (after 3rd round)
7. Game is over when one person gets 3 in a row or all squares filled (tie)

Objects
1. Game board - should be a list split into 3x3
2. Players - give input

Game Board
1. Create 3x3 board
2. Use a list to check for win/tie
3. 'tl' = list[0], 'tm' = list[1], 'tr' = list[2], etc
4. Check for 3 consecutive squares = 'x', board labelled above
5. Create algorithm for checking after each turn (starting with 3rd turn)

How do I store that a square has been played? How do I store those coordinates
as being filled? Dictionary? Every time a square is filled, coords[(x, y)]='x'
To test for the patterns I can just run a for loop through dictionary testing
[x] and [y] coordinates for matches?

coords = {
    (0,0): 'x'
    (0,1): 'x'
    (0,2): 'o'
    (1,0): 'x'  #match
    (1,1): 'x'  #match
    (1,2): 'x'  #match
    (2,0):
    (2,1):
    (2,2):
}

3 in a row occurs at:
    Horizontal: 012, 345, 678
    Vertical: 036, 147, 258
    \ Diagonal: 048
    / Diagonal: 246

'''

def createBoard():
    # create 9-cell board to play
    board = [x for x in range(9)]

    # print board in 3x3 square
    for x in range(9):
        if x in [2, 5, 8]:
            print(x, end='\n')
        else:
            print(x, end='|')

    return board

def checkWin(board, player):
    '''
    Board: is the list defined in createBoard()
    Player: string, is the character each player uses, i.e. 'x' or 'o'
    '''
    # define winning coordinates
    win = {
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    }

    # for each possible win row, check to see if each index matches player
    # if so, we have a winner
    # if not, search each remaining row
    # if still no winner, keep playing game
    winner = False
    for row in win:
        for index in row:
            if board[index] != player:
                winner = False
                break
            winner = True
        if winner:
            break

    return winner




board = createBoard()
board[6] = 'o'
board[7] = 'o'
board[8] = 'o'

print(checkWin(board, 'o'))
