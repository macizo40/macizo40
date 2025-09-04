#lets start with objects in python this is very similar to the java objects, lets see difference

#lets create a dictionary 

dictionary = [{'Name':'aldo','Lastname':'perez','id':'28375736473'},{'Name':'paco','Lastname':'melo','id':'78765577'}]

#then lets create a method that will show all the clients in the dictionary

def show_clients(clientnames, id):
    for c in clientnames:
        if (id == c ['id']):
            print ('{} {}'.format(c['Name'],c['Lastname']))
            return
    
    print ("client not found")

#lets work in a method that will delete the clients from the list 
def delete_client(clientnames, id):
    for i,c in enumerate(clientnames):
        if (id == c['id']):
            del( clientnames[i] )
            print(str(c),"> DELETED")
            return
        
    print('client not found')