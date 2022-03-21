def add(n1, n2):
    print(n1 + n2)


add(10, 20)

number1 = 10
number2 = input("Please type in a number.")
add(number1, number2)
try:
    # want to attempt
    # may have an error
    result = 10 + 10
except:
    print("Hey it looks like you aren't adding correctly.")
try:
    f = open("testfile", 'r')
    f.write("This is a test line.")
except TypeError:
    print("This is a type error!")
except OSError:
    print("This is a OS error!")
except:
    print("This is a new kind of error!")
finally:
    print("I always run!")
