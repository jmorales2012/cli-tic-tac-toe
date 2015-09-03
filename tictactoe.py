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
'''
import os
from random import randint


def createBoard():
    # create 9-cell board to play
    board = [' ' for x in range(9)]
    return board


def printBoard(board):
    # print board in 3x3 square
    os.system('clear')

    for x in range(9):
        if x in [2, 5, 8]:
            print(board[x], end='\n')
        else:
            print(board[x], end='|')


def updateBoard(move, symbol, board):
    '''
    move: an integer from playerInput/compInput
    symbol: a string char 'x' or 'o' depending on who's inputting
    '''
    board[move] = symbol
    return board


def checkWin(board, player):
    '''
    Board: is the list defined in createBoard()
    Player: string, is the symbol each player uses, i.e. 'x' or 'o'
    '''
    # define winning coordinates
    win = {
        (0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
        (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)
    }

    # for each possible win row, check if each index matches player tag 'x/o'
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


def playerInput(board):
    # Get player input, return as string
    # Check to make sure input is valid and not already on board
    while True:
        try:
            playerMove = int(input('Enter a # from 1-9: ')) - 1
            if board[playerMove] == 'x' or board[playerMove] == 'o':
                print('That spot is already taken. Please try again.')
            else:
                break
        except ValueError:
            print('Oops, not a valid number. Please try again.')
        except IndexError:
            print('Oops, number out of range. Please try again')

    return updateBoard(playerMove, 'x', board)


def compInput(board):
    # Select random # for computer to play
    compMove = randint(0, 8)
    while board[compMove] == 'x' or board[compMove] == 'o':
        compMove = randint(0, 8)

    return updateBoard(compMove, 'o', board)


if __name__ == '__main__':
    print('--------Tic Tac Toe--------')
    print('Cells are numbered 1-9 starting\nwith the top left corner.')

    board = createBoard()
    printBoard(board)

    win = False
    while not win:
        board = playerInput(board)
        printBoard(board)
        win = checkWin(board, 'x')
        if win:
            print('Player 1 wins!')
            break

        board = compInput(board)
        printBoard(board)
        win = checkWin(board, 'o')
        if win:
            print('Player 2 wins!')
            break
