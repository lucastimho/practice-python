lambda nums: nums**2


my_nums = [1, 2, 3, 4, 5, 6]
print(list(map(lambda nums: nums**2, my_nums)))


def check_even(num):
    return num % 2 == 0


for items in filter(check_even, my_nums):
    print(items)
