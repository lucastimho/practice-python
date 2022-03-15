def square(nums):
    return nums**2


my_nums = [1, 2, 3, 4, 5, 6]
for items in map(square, my_nums):
    print(items)
