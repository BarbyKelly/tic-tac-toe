import random

# Tic tac toe game base code followed from
# this tutorial: https://youtu.be/5s_lGC2sxwQ?feature=shared
# add to readme credit as well, tidy link

# Create a tic-tac-toe board
board = [' ' for x in range(10)]


def insert_letter(le, pos):
    board[pos] = letter


def free_space(pos):
    return board[pos] == ' '


def tictactoe_board(board):
    print('+--+--+--+--')
    print('|  |  |  |')
    print('| ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('|  |  |  |')
    print('+--+--+--+--')
    print('|  |  |  |')
    print('| ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('|  |  |  |')
    print('+--+--+--+--')
    print('|  |  |  |')
    print('| ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('|  |  |  |')

# Create a condition to determine the winner
def is_winner(bo, le):
    return
    (board [1] == le and bo[2] == le and bo[3] == le)
    or (board [4] == le and bo[5] == le and bo[6] == le)
    or (board [7] == le and bo[8] == le and bo[9] == le)
    or (board [1] == le and bo[4] == le and bo[7] == le)
    or (board [2] == le and bo[5] == le and bo[8] == le)
    or (board [3] == le and bo[6] == le and bo[9] == le)
    or (board [1] == le and bo[5] == le and bo[9] == le)
    or (board [7] == le and bo[5] == le and bo[3] == le)

# Create if board is full
def is_board_full(board):
    if board.count(' ') > 1:
        return False
    else:
        return True

# Create Welcome for the player. Add input option after - their name
# Add conditions when board is printed and when not
def main():
    print("Welcome to Tic Tac Toe")
    print(tictactoe_board)

    while not(is_board_full(board)):
        if not(is_winner(board, 'O')):
            player_move()
            tictactoe_board(board)
        else:
            print("Computer won this time. Thanks for playing!")
            break

        if not(is_winner(board, 'X')):
            comp_move()
            tictactoe_board(board)
        else:
            print("Congratulations! You won! Thanks for playing!")
            break

    if is_board_full(board):
        print("Tie! Thanks for playing!")

    

# Option to read instructions (i), play the game (p) or exit (e). "Type in the letter of your choice (i, p, or e) and then press Enter. 
# Create Error messages if they choose anything else than i, p, e. Letters only, and those letters only.

# Instructions:
# This version of Tic-Tac-Toe involves 2 players: website visitor vs computer and Tic-Tac-Toe board consisting 9 empty boxes.
# Before the game starts visitor will be asked to enter their initials.
# Computer's moves are marked with 0.
# Visitor's moves will be marked with an X.
# Both players take turns to mark the boxes on Tic-Tac-Toe board with their symbols.
# Visitor can mark their chosen empty box on the board with a number between 1-9, and then press Enter to confirm their choice.
# Each box can be chosen only once during each game.
# Goal of Tic-Tac-Toe is to get 3 of the same symbols in a straight line: vertically, horizontally or diagonally.
# Player who achieves to align their 3 symbols first in a straight continues line, is the winner.
# Game is over when one of the players wins, or when all of the boxes are filled, and game ends up in a tie.
# Once game is over, visitor has a choice to play again, exit the game or go over instructions again if they wish to do so.

# Create an option for the player to enter their name up to 10 characters or just initials? ("Please press 'Enter' after typing your name or initials")
# Create Error messages if not letters, if using symbols, if longer than 10 characters. Can you have an alert if they haven't pressed Enter after certain amount
# of time?

# Create Tic-Tac-Toe board with 1-9 empty boxes
# Choose if lines are needed around the boxes or does it look better without the lines. 

# Allocate 0 for computer and X for the visitor

# Game starts when visitor chooses their first box to be marked with their symbol
# Does visitor always start or can it be set on random, importing random?

# Create turn-taking: visitor, computer, visitor, computer, until one wins or it's a tie
# Create an Error message if visitor enters other than 1-9 number
# Create an Error message if visitor tries to fill a box/enter the number, that is already taken by the visitor or by the computer

# Create congratulations notice for when visitor wins
# Create a message: Better luck next time! when visitor loses
# Create a message: "It's a tie! Would you like to play again (p), go over instructions (i) or exit the game (e)? Make sure to press
# Enter after you have made your choice." Would it be possible to play, exit etc without pressing Enter?

# Create a message for all of the options: if visitor exits the game in the end or at the start, have an option to quit between or to go back to the instructions?
# Create notice of what happens if quitting during the game or if going back to instructions, new game will start when they return. Game can't be paused, saved?

# Exit the game. Have a message show up: "Thank you for visiting my Tic-Tac-Toe game site."

# Future development or this project: Add a score system "Visitor's name(initials) vs computer", add different symbols, add a time-limit, add an option best of 3 is the overall
# winner or best of 5, best of 10 