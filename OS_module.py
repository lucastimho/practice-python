import pwd
import os
# import shutil

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
# shutil.move('practice.txt', '/Users/lucasho/Acutalize')
# shutil.unlink(path) deletes a file at the path I decide
# shutil.rmdir(path) deletes an empty folder
# shutil.rmtree(path) removes all files and folers (dangerous)
# could always pip install send2trash