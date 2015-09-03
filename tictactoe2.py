"""Remake tictactoe.py using Classes/Methods"""
import os
import random


class Board():
    """
    Defines playing board in Tic Tac Toe game.

    Board() is the class that displays our game, accepts moves, and checks
    for winning conditions. Player() makes moves on Board() until a winner
    is found.

    Attributes:
        board: A list of 9 empty elements. Filled in with player symbols as
        game progresses.
    """

    def __init__(self):
        self.board = [' '] * 9

    def print_board(self):
        """Print game board in 3x3 layout centered on screen."""
        copy = self.board[:]
        print('\n')
        for x in range(9):
            if (x+1) % 3 == 0:
                print(copy[x], end='\n')
            else:

                print(copy[x], end='|')

    def update(self, move, symbol):
        """Update board with player move."""
        self.board[move] = symbol

    def check_win(self, symbol):
        """Checks board for winning line.

        Iterates through win set looking for matching lines for the player
        that calls this method.

        Args:
            symbol: Player character used to search for matching lines.

        Returns:
            True/False if a winning line is found.
        """
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

    def check_tie(self):
        """Checks to see if board is fully played or not.

        Iterates over board looking for blank spaces (not a tie) or looking
        for a full board (possible tie).

        Returns:
            True/False if board is full or not.
        """
        tie = False
        for x in range(9):
            if self.board[x] == ' ':
                tie = False
                break
            elif self.board[x] != ' ':
                tie = True
        return tie


class Player():
    """Defines a player in the game. Parent to Human() and Computer().

    Used to make moves on Board() throughout the game until a winner is found.

    Attributes:
        name: Name of the player
        winner: True/False if the player wins the game
        tie: True/False
    """

    def __init__(self, name):
        """Initialize Player() class with name, winner, & tie."

        Sets winner and tie to False when player is created. These attributes
        are used to determine if a player wins after their move.
        """
        self.name = name
        self.winner = False
        self.tie = False
        self.symbol = ' '


class Human(Player):
    """Defines a human-controlled player in the game.

    Makes moves and sets symbol based on user input.

    Attributes:
        symbol: Can be any 1-digit character. Used to fill in squares on board.
    """

    def set_symbol(self):
        self.symbol = input('\n{0}, enter your desired symbol: '.format(
            self.name))

        while len(self.symbol) != 1:
            self.symbol = input('\nYour symbol must be 1 character long: ')

    def make_move(self, board):
        """Asks for user input to make next move. Update & print board.

        Args:
            board: Board() is used to check for available moves
            and to call check_win() and check_tie()

        Returns:
            Sets self.winner and self.tie to their respective True/False. Used
            to determine if player won or if game ends in a tie.
        """
        while True:
            try:
                move = int(input('\n{0}, enter a # from 1-9: '.format(
                    self.name))) - 1
                if board.board[move] != ' ':
                    print('\nThat spot is already taken. Please try again.')
                else:
                    break
            except ValueError:
                print('\nOops, not a valid number. Please try again.')
            except IndexError:
                print('\nOops, number out of range. Please try again.')

        board.update(move, self.symbol)
        board.print_board()
        self.winner = board.check_win(self.symbol)
        self.tie = board.check_tie()


class Computer(Player):
    """Defines computer-controlled player in the game.

    Makes moves based on AI and common strategy to win game.

    Attributes:
        symbol: Default to 'O' unless already used by other player.
    """

    def set_symbol(self, otherPlayer):
        self.symbol = 'X'
        if self.symbol == otherPlayer.symbol:
            self.symbol = 'O'

    def get_move(self, board, otherPlayer):
        """Determine computer move based on AI strategy.

        Args:
            board: Board() is used to check for available moves
            player1: Player() is used to determine if computer can block next
            move by other player if that move would cause them to win game

        Returns:
            x: int in range(9) determined to be best move for computer.
        """
        copy = board.board[:]
        # corners are 0, 2, 6, 8 - only want empty corners
        corners = [x for x in range(0, 9, 2) if (x != 4) and (copy[x] == ' ')]
        # sides are 1, 3, 5, 7 - only want empty sides
        sides = [x for x in range(1, 8, 2) if (copy[x] == ' ')]

        # check if computer could win on next move, take it
        for x in range(9):
            if copy[x] == ' ':
                board.update(x, self.symbol)
                if board.check_win(self.symbol):
                    return x
                board.update(x, ' ')

        # check if other player could win on next move, block them
        for x in range(9):
            if copy[x] == ' ':
                board.update(x, otherPlayer.symbol)
                if board.check_win(otherPlayer.symbol):
                    return x
                board.update(x, ' ')

        # take an empty corner space next
        if len(corners) > 0:
            return random.choice(corners)

        # take an empty center next
        if copy[4] == ' ':
            return 4

        # take empty side last
        if len(sides) > 0:
            return random.choice(sides)

    def make_move(self, board, otherPlayer):
        """Make computer move official. Update & print board.

        Args:
            board: Board() is used to call update(), check_win(), check_tie()
            otherPlayer: Passed on to get_move() to make AI decision

        Returns:
            Sets self.winner and self.tie to their respective True/False. Used
            to determine if player won or if game ends in a tie.
        """

        move = self.get_move(board, otherPlayer)
        board.update(move, self.symbol)
        board.print_board()
        self.winner = board.check_win(self.symbol)
        self.tie = board.check_tie()


if __name__ == '__main__':
    print('\n')
    print('{:^80}'.format('----------Tic Tac Toe----------'), end='\n\n')
    print('{:^80}'.format('Cells are numbered 1-9 starting'))
    print('{:^80}'.format('with the top left corner.'))

    """
    1. Intro Screen
    2. Ask to play game
    3. Asks if player1 is human or computer
    4. Ask for name of player1
        1. If player1 is human, ask for symbol
    5. Asks if player2 is human or computer
    6. Asks for name of player2
        1. If player2 is human, ask for symbol
    7. Start game
    """

    game = Board()
    game.print_board()
    player1 = Computer('Josh')
    player2 = Computer('CPU')
    player1.set_symbol(player2)
    player2.set_symbol(player1)

    while True:

        player1.make_move(game, player2)
        if player1.winner:
            print('\nCongrats to {0} on winning!\n'.format(player1.name))
            break
        elif player1.tie and not player1.winner:
            print('\nTie game. Better luck next time.\n'.format(player1.name))
            break

        player2.make_move(game, player1)
        if player2.winner:
            print('\nCongrats to {0} on winning!\n'.format(player2.name))
            break
        elif player2.tie and not player2.winner:
            print('\nTie game.\n')
            break
