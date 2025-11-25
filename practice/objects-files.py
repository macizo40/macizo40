#now we will do something interesthing is to store the objects in a file which will be recovered with pickle

import pickle

#lets have a list of strings that we will create an object 

mylist = ['Dragon','Andromeda','Pegasus','Phoenix','Sygnus'] 

#lets create a class that will be stored in the file

class Saints:
    def __init__(self,constellation):
        self.constellation = constellation

    def __str__(self):
        return self.constellation

#we have not our class and lets have a list of objects type saints

my_saint_list = []

#lets create the objects in a dynamic way 

for i in mylist:
    saint = Saints(i) #every constellation name in the list will be a new saint
    my_saint_list.append(saint)

print("we can see now the list of saints with values {}".format(my_saint_list))

#it is time to create a file that will store these objects 

my_saint_file = open('practice/files/my_saint_file.pckl','wb')

#and store the list of objects there

pickle.dump(my_saint_list,my_saint_file) #list and file

my_saint_file.close()

#at this point the file has been written and we can now read the content

loaded_file = open('practice/files/my_saint_file.pckl','rb') #reading binary and pointer will be moved at the end

loaded_saints = pickle.load(loaded_file) #storing the content in a list 

#now lets use the str method that each object does have to read the content

for i in loaded_saints:
    print('from the file we got {}'.format(i))

loaded_file.close() #clossing always the file