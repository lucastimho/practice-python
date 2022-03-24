def create_cubes(n):
    result = []
    for x in range(n):
        yield x**3


print(list(create_cubes(10)))
