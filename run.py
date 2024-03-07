import random

# Code for this game learned from: https://youtu.be/dK6gJw4-NCo?feature=shared
""" Variables for tic-tac-toe """
board = [
    "-", "-", "-",
    "-", "-", "-",
    "-", "-", "-"]
currentPlayer = "X"
winner = None
gameRunning = True

""" Tic Tac Toe board """


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
    inp = int(input("Please enter a number between 1-9: "))
    if inp >= 1 and inp <= 9 and board[inp-1] == "-":
        board[inp-1] = currentPlayer
    else:
        print("Please try a different space!")


""" Check horizontal lines for win or tie """


def checkHorizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != "-":
        winner = board[1]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[4]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[7]
        return True


""" Check rows for win or tie"""


def checkRow(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[3]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[4]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[5]
        return True


""" Check diagonals for win or tie"""


def checkDiag(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[4]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[4]
        return True


""" Check for Tie """


def checkTie(board):
    global gameRunning
    if "-" not in board:
        printBoard(board)
        print("Tie!")
        gameRunning = False


""" Check for Win """


def checkWin():
    if checkDiag(board) or checkHorizontal(board) or checkRow(board):
        print(f"The winner is {winner}")


""" Switch the player """


def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"


""" Create computer's moves """


def computer(board):
    while currentPlayer == "O":
        position = random.randint(0, 8)
        if board[position] == "-":
            board[position] = "O"
            switchPlayer()


""" Check for win or tie after each turn """


while gameRunning:
    printBoard(board)
    playerInput(board)
    checkWin()
    checkTie(board)
    switchPlayer()
    computer(board)
    checkWin()
    checkTie(board)
