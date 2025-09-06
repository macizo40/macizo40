#now lets see the same implemtantion that we did in the past example with class and objects 

#name of the class, based that we will be having an object called Clients that will share same characteristics
class Client:
    #this like java we have a constructor method (called here init) that will assign the values recived in the call to their variables
    def __init__(self, id, name, lastname):
        self.id = id
        self.name = name
        self.lastname = lastname

    #this method was new for me, this is a way to return to screen in format string=str the content of the object usually with print   
    def __str__(self):
        return 'I am {} {}'.format(self.name,self.lastname)
    
#the class is as java a whole that will contains many things that a regular company does, including employees and clients data
class Company:
    
    #constructor will receive a set of objects from the Client class this needs a list of objects type Client
    def __init__(self, clients=[]):
        self.clients = clients

    #as we did in the previous excercise this is a simple method    
    def show_client(self, id=None):
        for c in self.clients:
            if c.id == id:
                print(c)
                return
        print("client not found")
    
    def delete_client(self, id=None):
        for i,c in enumerate(self.clients):
            if c.id == id:
                del(self.clients[i])
                print(str(c),"> BORRADO")
                return
        print("client not found")

#now lets do play with the objects

bob = Client("20","Bob","Terminator")
tom = Client("30","Tom","Byron")

#at this point there are two objects with a set of data that identifies each client information we can pass a list of them to Company

comp = Company(clients=[bob,tom])

#now that the class Company is ready we can play as we did with the show and delete

comp.show_client("10") #error this id does not exist
comp.show_client("30") #should not show the client Tom and his data

#now lets delete but now using the object that contains all data and not need to remember which ID we set 

comp.delete_client(tom) #not found since you need the id
comp.delete_client(tom.id) #succed since tom id was returned, but here the tom object is still alive 

#this will use the method __str__ of the object to do it more human readable.
print("Object tom is still alive and just was removed from the class company ==",tom)


comp.show_client(tom.id)

