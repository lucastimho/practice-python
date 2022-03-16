from secrets import choice
from turtle import position


print("Tic-Tac-Toe Game")
print("Here's how the board is laid out.")
print("7|8|9")
print("-----")
print("4|5|6")
print("-----")
print("1|2|3")

player1 = ''
player2 = ''
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
        player2 = 'O'
    else:
        player2 = 'X'


def player1_inputs():
    position = "no"
    while position not in range(1, 9):
        position = input(
            "Player 1, pick your position for your marker (1-9): ")
        if position not in range(1, 9):
            print("That is an invalid input! Try again. ")


def player2_inputs():
    position = "no"
    while position not in range(1, 9):
        position = input(
            "Player 2, pick your position for your marker (1-9): ")
        if position not in range(1, 9):
            print("That is an invalid input! Try again. ")
