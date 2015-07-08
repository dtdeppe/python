import os
import random
import string

def renamefiles():
    #variables
    path="/Users/ddeppe/Downloads/message"
    #get file names from a folder
    filelist = os.listdir(path)
    print (filelist)

    #for each file, rename filename
    os.chdir(path)
    savedpath=os.getcwd()
    print("current working directory is: ",savedpath)
    for filename in filelist:
        numberstring = random.choice(string.digits) + random.choice(string.digits)
        os.rename(filename,numberstring+filename)
        print("Old name: ",filename)
        print("New name: ",numberstring+filename)
        
renamefiles()
