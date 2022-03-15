def display(a, b, c):
    print(a)
    print(b)
    print(c)


row1 = ['', '', '']
row2 = ['', '', '']
row3 = ['', '', '']

display(row1, row2, row3)

position_index = input("Choose an index position: ")
print(row1[position_index])


def user_choice():
    choice = "yes"
    while choice.isdigit() == False:
        choice = input("Please enter a number (0-10): ")

        if choice.isdigit() == False:
            print("Sorry that is not a correct number")

    return int(choice)


user_choice()
