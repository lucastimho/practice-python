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
    acceptable_range = range(0, 10)
    within_range = False
    while choice.isdigit() == False or within_range == False:
        choice = input("Please enter a number (0-10): ")

        if choice.isdigit() == False:
            print("Sorry that is not a correct number")

        if choice.isdigit() == True:
            if int(choice) in acceptable_range:
                within_range = True
            else:
                print("Sorry you are out of the acceptable range (0-10)")
                within_range = False

    return int(choice)


user_choice()
