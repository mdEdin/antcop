import os

path = "./texts"

# Find all files in a directory and output their names

def searchFolder(path):
    if os.path.exists(path):
        files = os.listdir(path)
        files.sort()
        print("The files in the directory: " + path + " are" + "\n")
        for x in files:
            print(x)
    else: print ("There is no folder with the name " + path)
    print("\n")
    return files

# This a reference to the list of files found

allFiles = searchFolder(path)

def fileContents():
    os.chdir(path)
    print("File Contents\n")
    for x in allFiles:
        print(x)
        file = open(x, "rt")
        print(file.read() + "\n")

fileContents()
