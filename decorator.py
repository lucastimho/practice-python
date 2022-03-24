def func():
    return 1


def hello(name="Jose"):
    print("The hello() function has been executed!")

    def greet():
        return '\t This is the greet() func inside hello!'

    def welcome():
        return '\t This is the welcome() inside hello'

    print(greet())
    print(welcome())
    print("This is the end of the hello function!")
    if name == "Jose":
        return greet
    else:
        return welcome


my_new_func = hello("Jose")
print(my_new_func())
