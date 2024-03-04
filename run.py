import random

# Tic tac toe game base code followed from
# this tutorial: https://youtu.be/5s_lGC2sxwQ?feature=shared
# add to readme credit as well, tidy link

# Create a tic-tac-toe board. Single board better? Looks clearer?
board = [' ' for x in range(10)]


def insert_letter(le, pos):
    board[pos] = letter


def free_space(pos):
    return board[pos] == ' '


def tictactoe_board():
    print('+--+--+--+--')
    print('| 1 | 2 | 3 |')
    print('| ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('| 4 | 5 | 6 |')
    print('+--+--+--+--')
    print('| 7 | 8 | 9 |')
    print('| ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('|  |  |  |')
    print('+--+--+--+--')
    print('|  |  |  |')
    print('| ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('|  |  |  |')


# Create a condition to determine the winner
def is_winner(bo, le):
    return (
        (board[1] == le and bo[2] == le and bo[3] == le) or
        (board[4] == le and bo[5] == le and bo[6] == le) or
        (board[7] == le and bo[8] == le and bo[9] == le) or
        (board[1] == le and bo[4] == le and bo[7] == le) or
        (board[2] == le and bo[5] == le and bo[8] == le) or
        (board[3] == le and bo[6] == le and bo[9] == le) or
        (board[1] == le and bo[5] == le and bo[9] == le) or
        (board[7] == le and bo[5] == le and bo[3] == le)
    )


# Create player's move, guidelines and restrictions
def player_move():
    run = True
    while run:
        move = input("Please mark any empty box by typing a number (1-9)")
        try:
            move = int(move)
            if move > 0 and move < 10:
                if space_is_free(move):
                    run = False
                    insert_letter('X', move)
                else:
                    print("This box is occupied! Please try a different one.")
            else:
                print("Please type a number between 1-9")
        except error:
            print("Please type a number(1-9")


def comp_move():
    poss_move = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0

    for let in ['O', 'X']:
        for i in poss_move:
            board_copy = board[:]
            board_copy[i] = let
            if is_winner(board_copy, let):
                move = i
                return move

    corner_open = []
    for i in poss_move:
        if i in [1, 3, 7, 9]:
            corner_open.append(i)

    if len(corner_open) > 0:
        move = select_random(corner_open)
        return move

    if 5 in poss_move:
        move = 5
        return move

    edges_open = []
    for i in poss_move:
        if i in [2, 4, 6, 8]:
            edges_open.append(i)

    if len(edges_open) > 0:
        move = select_random(edges_open)

    return move


# Add random function for computer's moves
def select_random(li):
    ln = len(li)
    r = random.randrange(o, ln)
    return li(r)


# Create if board is full
def is_board_full(board):
    if board.count(' ') > 1:
        return False
    else:
        return True


# Create Welcome for the player. Add input option after - their name
# Add conditions when board is printed and when not
def main():
    print("Welcome to Tic Tac Toe \U000FEB68")
    print(tictactoe_board)

    while not (is_board_full(board)):
        if not (is_winner(board, 'O')):
            player_move()
            tictactoe_board(board)
        else:
            print("Computer wins this time. Thanks for playing!")
            break

        if not (is_winner(board, 'X')):
            move = comp_move()
            if move == 0:
                print("Tie! Thanks for playing!")
            else:
                insert_letter('O', board)
                print('Computer placed an \'O\' in position', move, ':')
                print_board(board)
        else:
            print("Congratulations! You won! Thanks for playing!")
            break

    if is_board_full(board):
        print("Tie! Thanks for playing!")
        

main()
