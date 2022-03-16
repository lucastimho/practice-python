# def display(a, b, c):
#     print(a)
#     print(b)
#     print(c)


# row1 = ['', '', '']
# row2 = ['', '', '']
# row3 = ['', '', '']

# display(row1, row2, row3)

# position_index = input("Choose an index position: ")
# print(row1[position_index])


# def user_choice():
#     choice = "yes"
#     acceptable_range = range(0, 10)
#     within_range = False
#     while choice.isdigit() == False or within_range == False:
#         choice = input("Please enter a number (0-10): ")

#         if choice.isdigit() == False:
#             print("Sorry that is not a correct number")

#         if choice.isdigit() == True:
#             if int(choice) in acceptable_range:
#                 within_range = True
#             else:
#                 print("Sorry you are out of the acceptable range (0-10)")
#                 within_range = False

#     return int(choice)


# user_choice()

game_list = [0, 1, 2]


def display_game(game_list):
    print("This is the current game list: ")
    print(game_list)


display_game(game_list)


def postion_choice():
    choice = "wrong"

    while choice not in ['0', '1', '2']:
        choice = input("Pick a postion (0, 1, 2): ")

        if choice not in ['0', '1', '2']:
            print("Sorry invalid input.")

    return int(choice)


postion_choice()
