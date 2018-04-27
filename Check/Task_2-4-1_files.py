import os

path = "D:\\Downloads\\main"
PyDirList = list()

for current_dir, dirs, files in os.walk(path):
    for file in files:
        if file.endswith(".py"):
            PyDirList.append(current_dir)
sorted(PyDirList)
print(PyDirList)
