#lets start with objects in python this is very similar to the java objects, lets see difference

#lets create a dictionary 

dictionary = [{'Name':'aldo','Lastname':'perez','id':'28375736473'},{'Name':'paco','Lastname':'melo','id':'78765577'}]

print("Dictionary is BOF {}".format(dictionary))

#then lets create a method that will show all the clients in the dictionary
"""
Method that will show the clients objects in the dictionary
"""
def show_clients(clientnames, id):
    for c in clientnames:
        if (id == c ['id']):
            print("Found a client as {} {}".format(c['Name'],c['Lastname']))
            return
    print(f"The search of client with id= '{id}', was not found")

#lets work in a method that will delete the clients from the list 
"""
This method will delete the client from the list of objects.
"""
def delete_clients(clientnames, id):
    for i,c in enumerate(clientnames):
        if (id == c['id']):
            del(clientnames[i])
            print("I found the client:",str(c),"> DELETED")
            return
    print(f"Trying to delete client with id= '{id}',is not possible, client was not found")

#now that we have a list and methods it is time to try to find with the first method the client name

show_clients(dictionary,'28375736473')

#now lets try to show a client that does not exist

show_clients(dictionary,'2837573')

#now let's try to delete de client from the dictionary that does not exist

delete_clients(dictionary,'2837573')

#now lets delete one tht yes it does exist

delete_clients(dictionary,'28375736473')

#lets try to see that the deleted user was not any more in the dictionary 

print("Dictionary is EOF {}".format(dictionary))


