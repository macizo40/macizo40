#now we will be working with bring the lines of the file, replace one of them and put it back to the file

from io import open

myfile = open('practice/files/mypointer.txt','r+')

lines = myfile.readlines()

print("here are the lines of the file:\n",lines)

#the last line is something that went wrong in the past excersice so we will replace it with something with format

lines[-1] = "No more a wrong word line"

print("a new line added to the array:\n",lines)

myfile.seek(0)

myfile.writelines(lines)

myfile.close()