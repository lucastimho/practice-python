def myfunc(a, b):
    # return 5% of the sum
    return sum((a, b)) * 0.05


def myfunc(*args):
    return sum((args)) * 0.05


def myfunc(**kwargs):
    print(kwargs)
    if 'fruits' in kwargs:
        print('My fruit of choice is {}'.format(kwargs['fruits']))
    else:
        print('I did not find any fruits here')
