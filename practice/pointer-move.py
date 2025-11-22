from io import open

#now lets try to see how the pointer moves, at the moment that we do open a file the pointer is in the first line first character

#lets use a method to move the pointer to the 10 position of the line

#using the pointer file - pointer is in the first position
myfile = open('practice/files/mypointer.txt','r')

print('pointer is here ->',myfile.seek(10))

print('this should skip 10 characters \n',myfile.read())

print("this last read should say nothing:", myfile.read())

print("we will put the pointer back at the begining ->", myfile.seek(0))

print("We can now again read all the file\n",myfile.read())

#lets again set the pointer to the begining
myfile.seek(0)

#now with the use of the read, we will just return 10 characters and the pointer will be in the 11

print("reading just 10 characters:",myfile.read(10))

#if we read now again, the pointer is in the 11 position and will not print the previous ones

print("reading the lines from the last position:\n",myfile.read())

#remember that we can read a line, so if we move the pointer to the first position we can use the read line

myfile.seek(0)

print("lets see lenght of the first line with this:\n",len(myfile.readline()))

#with that we can play with move the seek like this

print("at the half of the first line:\n",myfile.seek(len(myfile.readline())/2))

print("now we will reading from the half to next:\n",myfile.read())

myfile.close()
