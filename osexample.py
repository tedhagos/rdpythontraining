import os

dirname = "/Users/ted/PycharmProjects/rdpythontrainin"

try:

except:

os.chdir(dirname)
for file in os.listdir("."):
    info = os.stat(file)
    print("%-20s: size %d" % (file, info.st_size))

