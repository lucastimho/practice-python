from secrets import choice


print("Tic-Tac-Toe Game")
print("Here's how the board is laid out.")
print("7|8|9")
print("-----")
print("4|5|6")
print("-----")
print("1|2|3")

player1 = ''
player2 = ''


def player():
    while player1 not in ['X', 'O']:
        player1 = input("Player 1, choose either X or O. ")
        player1 = str(player1)
        if player1 not in ['X', 'O']:
            print("I do not understand. Please pick either X or O")
    return player1


if player1 == 'X':
    player2 = 'O'
else:
    player2 = 'X'
