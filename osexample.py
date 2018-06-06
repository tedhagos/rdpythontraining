import os

dirname = "/Users/ted/PycharmProjects/rdpythontrainin"

os.chdir(dirname)
for file in os.listdir("."):
    info = os.stat(file)
    print("%-20s: size %d" % (file, info.st_size))

