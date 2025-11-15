#on this one we will be doing reading from the files and save the data in some elements

from io import open

#files have different modes, so to write in a file, it needs to be open, so lets create one

myfile = open('practice/files/myfile.txt','r')

mystring = myfile.read()

print("content of the files is ",mystring)

#this method finalize the use and the write
myfile.close()
