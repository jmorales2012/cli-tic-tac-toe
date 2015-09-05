"""Remake tictactoe.py using Classes/Methods"""
import os
import random


class Board():
    """Defines playing board in Tic Tac Toe game.

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
        """Print game board in 3x3 layout."""
        self.instructions()
        print('\n')
        for x in range(0, 9, 3):
            print('{:^80}'.format('|'.join(self.board[x:x+3])))

    def instructions(self):
        """Prints instructions to screen above board every move."""
        os.system('clear')
        print('\n')
        print('{:^80}'.format('-----------Tic Tac Toe-----------'), end='\n\n')
        print('{:^80}'.format('Squares are numbered 1-9 starting'))
        print('{:^80}'.format('with the top left corner.'))

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

    def set_symbol(self, otherPlayer=0):
        """If this is 2nd player, want to make sure symbols don't match."""
        self.symbol = input('{0}, enter your desired symbol: '.format(
            self.name))

        if otherPlayer:
            while self.symbol == otherPlayer.symbol:
                self.symbol = input(
                    'Your symbol can\'t match player 1\'s symbol: ')

        while len(self.symbol) != 1:
            self.symbol = input('Your symbol must be 1 character long: ')

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
                    print('That spot is already taken. Please try again.')
                else:
                    break
            except ValueError:
                print('Not a valid number. Please try again.')
            except IndexError:
                print('Number out of range. Please try again.')

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

    def set_symbol(self, otherPlayer=0):
        """If another player exists, make sure symbols don't match."""
        self.symbol = 'X'
        if otherPlayer:
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


def playMenu():
    """Asks user if they want to play game. Calls makeChoice() for input.

    Returns:
        Returns an integer (1 or 2) based on user input from makeChoice().
        1 means yes they want to play
        2 means no they don't want to play
    """

    print('\nDo you wan\'t to play Tic Tac Toe?', end='\n')
    print('\n1. Enter 1 to Play')
    print('2. Enter 2 to Exit', end='\n')

    return makeChoice()


def playerSelection(player):
    """Asks user if that specific player is a human or computer.

    Returns:
        Returns 1 or 2 based on user input from makeChoice().
        1 means that this player is a Human()
        2 means that this player is a Computer()
    """
    print('\nIs player {} a human or computer?'.format(player))
    print('1. Enter 1 if Human')
    print('2. Enter 2 if Computer')

    return makeChoice()


def makeChoice():
    choice = input('\nEnter your choice: ')

    while choice not in ['1', '2']:
        choice = input('Oops, invalid choice. Try again: ')

    return int(choice)


def createPlayer(playerChoice, otherPlayer=0):
    """Create a Player() class depending on user's input.

    Args:
        playerChoice: Will be 1 or 2 depending if user selected Human/Computer
        otherPlayer: Used to make sure the symbols don't match

    Returns:
        Returns either a Human() or Computer() class with their name and
        symbol set for the game.
    """
    # create Human() player
    if playerChoice == 1:
        name = input('Enter your name: ')
        player = Human(name)
        player.set_symbol(otherPlayer)

    # create Computer() player
    elif playerChoice == 2:
        name = input('Enter computer\'s name: ')
        player = Computer(name)
        player.set_symbol(otherPlayer)

    return player


if __name__ == '__main__':
    """
    1. Intro Screen
    2. Ask to play game
    3. Asks if player1 is human or computer
    4. Ask for name of player1
        1. If player1 is human, ask for name & symbol
    5. Asks if player2 is human or computer
    6. Asks for name of player2
        1. If player2 is human, ask for name & symbol
    7. Start game
    """

    playing = True
    # allows user to decide if they want to play game or not
    playGame = playMenu()

    if playGame == 1:
        # create players 1 and 2 depending on choice to be human/computer
        player1 = createPlayer(playerSelection(1))
        player2 = createPlayer(playerSelection(2), player1)
        # create game to play
        game = Board()
        game.print_board()

    elif playGame == 2:
        print('{:^80}'.format('See you next time!'))
        playing = False

    while playing:

        # if the player is a Computer, they pass different args then Human
        if isinstance(player1, Computer):
            player1.make_move(game, player2)
        else:
            player1.make_move(game)

        if player1.winner:
            print('\n' + '{:^80}'.format(
                'Congrats to %s on winning!\n') % (player1.name))
            break
        elif player1.tie and not player1.winner:
            print('\n' + '{:^80}'.format(
                'Tie. Better luck next time %s.\n') % (player1.name))
            break

        # same as above, determining if player is a computer
        if isinstance(player2, Computer):
            player2.make_move(game, player1)
        else:
            player2.make_move(game)

        if player2.winner:
            print('\n' + '{:^80}'.format(
                'Congrats to {0} on winning!\n') % (player2.name))
            break
        elif player2.tie and not player2.winner:
            print('\n' + '{:^80}'.format('Tie game.\n'))
            break
