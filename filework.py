import os
print("Present Working Directory is: " + os.getcwd())
dname =input("Enter the directory that you want to refer : " )
os.chdir(dname)
print("Present Working Directory is: " + os.getcwd())

# print all files & folders recursively
for dirpath, dirnames, filenames in os.walk("."):
    # iterate over directories
    for dirname in dirnames:
        print("Directory:", os.path.join(dirpath, dirname))
    # iterate over files
    for filename in filenames:
        print("File:", os.path.join(dirpath, filename))
