import os

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
        os.rename(filename, filename.strip("0123456789"))
        print("Old name: ",filename)
        print("New name: ",filename.strip("0123456789"))
        
renamefiles()
