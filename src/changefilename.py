import os
os.chdir('ch02')
print(os.listdir())
for oldfilename in os.listdir():
    if oldfilename[-2:] == "py":
        newfilename = "p" + oldfilename
        print(oldfilename)
        print(newfilename)
        os.rename(oldfilename,newfilename)
        print()

