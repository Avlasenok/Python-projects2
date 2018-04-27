import os

winpath = "D:\\Downloads\\main"
# macpath = "/Users/avlasenok/Downloads/main"
PyDirList = list()

for current_dir, dirs, files in os.walk(winpath):
    for file in files:
        if file.endswith(".py"):
            PyDirList.append(current_dir)
sorted(PyDirList)
print(PyDirList)
