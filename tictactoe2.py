'''
Remake tictactoe.py using Classes/Methods
'''
import os
from random import randint


class Board():
    '''
    Board() is the class that displays our game, accepts moves, and checks
    for winning conditions. Player() makes moves on Board() until a winner
    is found.
    '''

    def __init__(self):
        self.board = [' ' for x in range(9)]

    def print_board(self):
        '''
        Print our game board in a 3x3 layout
        '''
        os.system('clear')
        for x in range(len(self.board)):
            if (x+1) % 3 == 0:
                print(self.board[x], end='\n')
            else:
                print(self.board[x], end='|')

    def update(self, move, symbol):
        '''
        Updates board with current move. Also checks if winner was found.
        Returns True/False to Player() depending on winner/no winner.
        move: refers to a move by a player/computer
        symbol: refers to that player's symbol
        '''
        self.board[move] = symbol
        self.print_board()
        return self.check_win(symbol)

    def check_win(self, symbol):
        '''
        Check to see if 3-in-a-row match was made
        Returns True/False to self.update() if a winner was found
        symbol: refers to specific player's symbol
        '''
        # define winning coordinates
        win = {
            (0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
            (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)
        }

        # for each possible win row, check if each index matches player symbol
        winner = False
        for row in win:
            for index in row:
                if self.board[index] != symbol:
                    winner = False
                    break
                winner = True
            if winner:
                break

        return winner

    def check_tie(self, symbol):
        tie = False
        for x in range(len(self.board)):
            if self.board[x] == ' ':
                tie = False
                break
            elif self.board[x] != ' ' and not self.check_win(symbol):
                tie = True
        return tie


class Player():
    '''
    Player() is the class that defines each player, human or computer. Player()
    makes moves on Board() throughout the game until a winner is found.
    '''

    def __init__(self, name):
        '''
        symbol: refers to the char the player wants to use on the board
        winner = set to False to start game
        '''
        self.name = name
        self.winner = False
        self.tie = False
        self.symbol = input('{0}, enter your desired symbol: '.format(
            self.name))

        while len(self.symbol) != 1:
            self.symbol = input('Your symbol must be 1 character long: ')

    def make_move(self, board):
        '''
        Lets the player make a move. Must be a valid # from 1-9, no letters.
        Calls Board().update() to update the game board and check for a winner.
        If True (winner), call winner() function

        board: reference to Board.board to check for available moves
        playing: True/False, used to keep playing or end game if winner
        '''
        while True:
            try:
                move = int(input('{0}, enter a # from 1-9: '.format(
                    self.name))) - 1
                if board.board[move] != ' ':
                    print('That spot is already taken. Please try again.')
                else:
                    break
            except ValueError:
                print('Oops, not a valid number. Please try again.')
            except IndexError:
                print('Oops, number out of range. Please try again.')

        self.winner = board.update(move, self.symbol)
        self.tie = board.check_tie(self.symbol)


if __name__ == '__main__':
    print('----------Tic Tac Toe----------')
    print('Cells are numbered 1-9 starting\nwith the top left corner.')

    game = Board()
    game.print_board()
    player1 = Player('Jim')
    player2 = Player('Bob')

    while True:

        player1.make_move(game)
        if player1.winner:
            print('Congrats to {0} on winning!'.format(player1.name))
            break
        elif player1.tie:
            print('Tie game.')
            break

        player2.make_move(game)
        if player2.winner:
            print('Congrats to {0} on winning!'.format(player2.name))
            break
        elif player2.tie:
            print('Tie game.')
            break
