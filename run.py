import random

# Tic tac toe game original base code followed from
# this tutorial: https://youtu.be/5s_lGC2sxwQ?feature=shared
# add to readme credit as well, tidy link

# Create a tic-tac-toe board.
# variables adj based on: https://youtu.be/dK6gJw4-NCo?feature=shared
# board learned from Code Coach video
""" Variables for tic-tac-toe """
board = [
    "-", "-", "-",
    "-", "-", "-",
    "-", "-", "-"]
currentPlayer = "X"
winner = None
gameRunning = True


# Board - origin styling from https://youtu.be/5s_lGC2sxwQ?feature=shared
# Board style edit based on: https://youtu.be/dK6gJw4-NCo?feature=shared
# Style the board. for now similar to code coach. edit spaces, pluses
def printBoard(board):
    print('+---+---+---+')
    print('| ' + board[0] + ' | ' + board[1] + ' | ' + board[2] + ' |')
    print('+---+---+---+')
    print('| ' + board[3] + ' | ' + board[4] + ' | ' + board[5] + ' |')
    print('+---+---+---+')
    print('| ' + board[6] + ' | ' + board[7] + ' | ' + board[8] + ' |')
    print('+---+---+---+')


""" Add Player input """
def playerInput(board):
    inp = int(input("Please enter a number between 1-9 and press Enter: "))
    if inp >= 1 and inp <= 9 and board[inp-1] == "-":
        board[inp-1] = currentPlayer
    else:
        print("Please choose a different space!")


""" Check for win or tie after each turn """
while gameRunning:
    printBoard(board)
    playerInput(board)
