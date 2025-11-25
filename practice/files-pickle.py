#noe we want to learn more about the files methods.

#importing this library
import pickle

#lets try this, to store a list in the file

mylist = ['Nona','Oppa','Boarding','Market']

#open a file is the same as before we need to set the path 
#for this we will use a different extension and the wb means write in binary
myfile = open('practice/files/myfile.pckl','wb')

#using the common method dump is to just write and replace all in the file anytime that is called.

pickle.dump(mylist,myfile) #as you can see there is a need to specify two parameters.

myfile.close()

#now lets see if we can recover the data from the file in a new list

myfile2 = open('practice/files/myfile.pckl','rb') #this time opening as read in binary

myNewList = pickle.load(myfile2) #important is that after the load the pointer is at the end of the file

print("content in the new list is {}".format(myNewList))

myfile2.close()