from io import open

#now lets start to test the areas where the open can read lines by lines and pointer does work

#using the pointer file
myfile = open('practice/files/mypointer.txt','r')

#the readline does return empty is it is the EOF so we will loop until this comes upfront

while myfile.readline() != '':
    line = myfile.readline()
    print("here->",line)


myfile.close()