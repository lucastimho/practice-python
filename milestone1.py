print("Tic-Tac-Toe Game")
print("Here's how the board is laid out.")
print("7|8|9")
print("-----")
print("4|5|6")
print("-----")
print("1|2|3")

board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']


def board_state():
    print(board[6]+"|"+board[7]+"|"+board[8])
    print("-----")
    print(board[3]+"|"+board[4]+"|"+board[5])
    print("-----")
    print(board[0]+"|"+board[1]+"|"+board[2])


def player():
    while player1 not in ['X', 'O']:
        player1 = input("Player 1, choose either X or O. ")
        player1 = str(player1)
        if player1 not in ['X', 'O']:
            print("I do not understand. pick either X or O")
    if player1 == 'X':
        player2 = player2 + 'O'
    else:
        player2 = player2 + 'X'
    return player1, player2


def player1_inputs():
    position = "no"
    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        position = input(
            "Player 1, pick your position for your marker (1-9): ")
        position = int(position)
        if position not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            print("That is an invalid input! Try again. ")
        else:
            board[position - 1] = player1


def player2_inputs():
    position = "no"
    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        position = input(
            "Player 2, pick your position for your marker (1-9): ")
        position = int(position)
        if position not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            print("That is an invalid input! Try again. ")
        else:
            board[position - 1] = player2


def win_state():
    if board[0] == board[1] and board[0] == board[2] and board[0] != ' ':
        return False
    elif board[0] == board[4] and board[0] == board[8] and board[0] != ' ':
        return False
    elif board[6] == board[4] and board[6] == board[2] and board[6] != ' ':
        return False
    elif board[3] == board[4] and board[3] == board[5] and board[3] != ' ':
        return False
    elif board[6] == board[7] and board[6] == board[8] and board[6] != ' ':
        return False
    elif board[0] == board[3] and board[0] == board[6] and board[0] != ' ':
        return False
    elif board[1] == board[4] and board[1] == board[7] and board[1] != ' ':
        return False
    elif board[2] == board[5] and board[2] == board[8] and board[2] != ' ':
        return False
    elif board[6] == board[7] and board[6] == board[8] and board[6] != ' ':
        return False
    else:
        return True


player1 = ''
player2 = ''

while player1 not in ['X', 'O']:
    player1 = input("Player 1, choose either X or O. ")
    player1 = str(player1)
    if player1 not in ['X', 'O']:
        print("I do not understand. pick either X or O")
    if player1 == 'X':
        player2 = player2 + 'O'
    else:
        player2 = player2 + 'X'


def game():
    while win_state():
        if win_state():
            player1_inputs()
            board_state()
        if win_state():
            player2_inputs()
            board_state()
    print("Tic-Tac-Toe!")


game()
