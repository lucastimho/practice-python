import time

def func_one(n):
  return [str(num) for num in range(n)]

def func_two(n):
  return list(map(str, range(n)))

start = time.time()
func_one(1000000)
end = time.time()
print(end - start)
start = time.time()
func_two(1000000)
end = time.time()
print(end - start)