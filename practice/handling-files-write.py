#it is time to start saving our work in the files in the disk space this will save the activity.
#files handling is an advance package so you need to import io

from io import open



#files have different modes, so to write in a file, it needs to be open, so lets create one

myfile = open('practice/files/myfile.txt','w')
for i in range(10):
    #now lets start with something simple, we do have elements like a text
    mystring = f"Hello I am line number {i} and I want to be save in a file\n"
    myfile.write(mystring)
#this method finalize the use and the write
myfile.close()

#by running all the previous code, the file will be saved again and again overwritting the content and will looks like does not change