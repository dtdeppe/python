import os

def renamefiles():
    #get file names from a folder
    filelist = os.listdir(r"/Users/ddeppe/Downloads/prank")
    print (filelist)

    #for each file, rename filename
    os.chdir(r"/Users/ddeppe/Downloads/prank")
    savedpath=os.getcwd()
    print("current working directory is: ",savedpath)
    for filename in filelist:
        os.rename(filename, filename.strip("0123456789"))
        print("Old name: ",filename)
        print("New name: ",filename.strip("0123456789"))
        
renamefiles()
