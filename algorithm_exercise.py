def increase_seven(x):
    for n in x:
        return n + 7


def return_string_length(x):
    for n in x:
        return len(n)


def divide_by_two(x):
    for n in x:
        return n / 2


def return_first_char(x):
    for n in x:
        return n[0]


def stringify(x):
    for n in x:
        return str(n)


def even_numbers(x):
    for n in x:
        if n % 2 == 0:
            return n


def less_than_four_char(x):
    for n in x:
        if len(n) < 4:
            return n


def less_than_ten(x):
    for n in x:
        if n < 10:
            return n


def exclude_b(x):
    for n in x:
        if n[0] != "b":
            return n
