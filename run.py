import random

# Code for this game learned from: https://youtu.be/dK6gJw4-NCo?feature=shared
# Variables for tic-tac-toe
board = [
    "-", "-", "-",
    "-", "-", "-",
    "-", "-", "-"]
currentPlayer = "X"
winner = None
gameRunning = True


def printBoard(board):
    """Tic Tac Toe board"""
    print('+---+---+---+')
    print('| ' + board[0] + ' | ' + board[1] + ' | ' + board[2] + ' |')
    print('+---+---+---+')
    print('| ' + board[3] + ' | ' + board[4] + ' | ' + board[5] + ' |')
    print('+---+---+---+')
    print('| ' + board[6] + ' | ' + board[7] + ' | ' + board[8] + ' |')
    print('+---+---+---+')


def playerInput(board):
    """Add Player input"""
    while True:
        inp = int(input("Please enter a number between 1-9: "))
        if inp >= 1 and inp <= 9 and board[inp-1] == "-":
            board[inp-1] = currentPlayer
            break
        else:
            print("Please try a different space!")
        

def checkHorizontal(board):
    """Check horizontal lines for win or tie"""
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


def checkRow(board):
    """Check rows for win or tie"""
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


def checkDiag(board):
    """Check diagonals for win or tie"""
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[4]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[4]
        return True


def checkTie(board):
    """Check for Tie"""
    global gameRunning
    if "-" not in board:
        printBoard(board)
        print("Tie!")
        exit()
       

def checkWin():
    """Check for Win"""
    if checkDiag(board) or checkHorizontal(board) or checkRow(board):
        printBoard(board)
        print(f"The winner is {winner}. Congratulations!")
        exit()
     

def switchPlayer():
    """Switch the player"""
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"


def computer(board):
    """Create computer's moves"""
    while currentPlayer == "O":
        position = random.randint(0, 8)
        if board[position] == "-":
            board[position] = "O"
            switchPlayer()


while gameRunning:
    """Check for win or tie after each turn"""
    printBoard(board)
    playerInput(board)
    checkWin()
    checkTie(board)
    switchPlayer()
    computer(board)
