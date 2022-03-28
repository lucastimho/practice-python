import pwd
import os

pwd
# Opens, writes, and close txt file
# f = open("practice.txt", "w+")
# f.write("This is a test string")
# f.close()
path = os.getcwd()
print(path)
list = os.listdir(path)
for p in list:
  print(p)