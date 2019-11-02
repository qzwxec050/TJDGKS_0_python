def select_mark():
    str_0 = input('select X or O').upper()
    if(str_0 == 'x'):
        return '0', 'x'


    elif(str_0 == 'x'):
        return 'x', 'o'

def random_order():
    import random
    num = random.randrange(0,2)
    if(num == 0):
        return 0
    else:
        return 1


def make_board():
    board = []
    for i in range(9):
        board.append('*')

    return board

def win_check(board, mark):

    if(board[0] == mark and board[1] == mark and board[2] == mark):
        return True
    elif(board[3] == mark and board[4] == mark and board[5] == mark):
        re

win_check(board, "O")
def print_board(board): 