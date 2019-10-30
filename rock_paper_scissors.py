# Python 3

from sys import exit
from random import choice
from colorama import init, Fore, Style

MOVES = ["rock", "paper", "scissors"]


class Player:

    # """This class represents a dumb player that always plays "rock."
    # All other players inherit from this class.
    #
    # Attributes:
    #     other_previous_move (str): The previous opponent's move
    #     own_previous_move (str): The player's own previous move
    #     score (int): The current score of the player
    # """

    def __init__(self):
        # """Initializes the player class.
        # When the game starts, all players have randomly attributed previous
        # moves both for themselves and for their opponents.
        # """
        self.score = 0
        self.own_previous_move = choice(MOVES)
        self.other_previous_move = choice(MOVES)

    def move(self):
        # """A single move of the player.

        # Returns:
        #     str: Always returns "rock"
        # """
        return "rock"

    def learn(self, my_move, their_move):
        # """Updates the previous moves for the player and its opponent.
        #
        # Args:
        #     my_move (str): The player's own previous move
        #     their_move (str): The opponent's previous move
        # """
        self.own_previous_move = my_move
        self.other_previous_move = their_move


class RandomPlayer(Player):

    # """This class represents a player that always picks a random move."""

    def move(self):
        # """Pick a random move from the global list of moves.

        # Returns:
        #     str: A random move from the global list of moves
        # """
        return choice(MOVES)


class ReflectPlayer(Player):

    # """This class represents a player that always mimics the opponent's
    # previous move.
    # """

    def move(self):
        # """Pick the opponent's previous move.
        #
        # Returns:
        #     str: The opponent's previous move
        # """
        return self.other_previous_move


class CyclePlayer(Player):

    # """This class represents a player that cycles through the list of global
    # moves. When it reaches the end of the list, it restarts from the beginning.
    # """

    def move(self):
        # """Play the next move on the list of global moves. If there are no more
        # moves in the list, then play the first one.
        #
        # Returns:
        #     str: The next move in the list of global moves, or the first move
        #     in the list, if there are no more moves.
        # """
        index = MOVES.index(self.own_previous_move)
        if index == 2:
            return MOVES[0]
        else:
            return MOVES[index + 1]


class HumanPlayer(Player):

    # """This class represents a human player.
    # """

    def move(self):
        # """The human player can choose a move from the list of global moves.
        # If the player types the move incorrectly, they are asked to pick their
        # move again.
        #
        # Returns:
        #     str: A move from the list of global moves
        # """
        player_move = ""

        while True:
            player_move = input(("Please, enter your move "
                                 "(rock, paper, or scissors): "))
            # """ If the chosen move is incorrect, inform the user and prompt
            # them to enter a new move.
            # """
            if (player_move.lower() not in MOVES):
                print("Invalid move!")
                continue
            else:
                break

        return player_move


def beats(one, two):
    # """Determine whether or not the player's move beats the opponent's move.
    # Rock beats scissors, scissors beat paper, and paper beats rock.
    #
    # Args:
    #     one (str): The player's move
    #     two (str): The opponent's move
    #
    # Returns:
    #     bool: True if the player's move beats the opponent's move,
    #     false otherwise
    # """
    return ((one == "rock" and two == "scissors") or
            (one == "scissors" and two == "paper") or
            (one == "paper" and two == "rock"))


class Game:

    # """A single game of rock, paper, scissors, composed of 7 rounds.
    # The player who wins a round gets 1 points. The player with the higher score
    # at the end of the 7 rounds wins the game.
    #
    # Attributes:
    #     p1 (Player): The first player
    #     p2 (Player): The second player
    # """

    def __init__(self, p1, p2):
        # """Initialize the game.
        #
        # Args:
        #     p1 (Player): The first player
        #     p2 (Player): The second player
        # """
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        # """One single round of rock, paper, scissors. Each player picks a move,
        # the score for each player is calculated and the moves are remembered.
        # """
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1} Player 2: {move2}")
        self.keep_score(move1, move2)
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        # """Print the intro message, and plays 7 rounds of the game. At the end
        # of the 7 rounds, announce the winner.
        # """
        print(Style.BRIGHT, Fore.YELLOW)
        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("~~~~ Welcome to a new Rock, Paper, Scissors game! ~~~~")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("\nLet's get started!")
        for round in range(7):
            print(Fore.YELLOW)
            print(f"\nRound {round}:")
            try:
                self.play_round()
            # """ If the player interrupts the game, exit gracefully """
            except KeyboardInterrupt:
                exit(0)
        print(Fore.YELLOW)
        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("~~~~~~~~~~~~~~~~~ GAME OVER! ~~~~~~~~~~~~~~~~~")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        if self.p1.score > self.p2.score:
            print(Fore.GREEN)
            print("And the winner is... PLAYER 1!")
        elif self.p2.score > self.p1.score:
            print(Fore.MAGENTA)
            print("And the winner is... PLAYER 2!")
        else:
            print(Fore.CYAN)
            print("There is no winner! It was a draw!")

    def keep_score(self, move1, move2):
        # """Keep the scores for both players. Print the round's winner and the
        # updated scores. In case of a tie, print a tie message and the current
        # scores.
        #
        # Args:
        #     move1 (str): The first player's move
        #     move2 (str): The second player's move
        # """
        if beats(move1, move2):
            self.p1.score += 1
            print(Fore.GREEN)
            print(f"{move1} beats {move2}! Player 1 wins this round!")
        elif beats(move2, move1):
            self.p2.score += 1
            print(Fore.MAGENTA)
            print(f"{move2} beats {move1}! Player 2 wins this round!")
        else:
            print(Fore.CYAN)
            print("This was a tie!")
        print(Fore.GREEN)
        print(f"Player 1 Score: {self.p1.score}")
        print(Fore.MAGENTA)
        print(f"Player 2 Score: {self.p2.score}")


if __name__ == "__main__":
    game = Game(RandomPlayer(), HumanPlayer())
    # """ Initialize colorama to display colored text on the console """
    init()
    game.play_game()
