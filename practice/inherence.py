#lets now practice as java to pass methods and attributes from a parent class to child class

class Product:

    def __init__(self,reference,type,name,description):
        self.reference = reference
        self.name = name
        self.type = type
        self.description = description
        
    def __str__(self):
        return "Reference={},Name={}".format(self.reference,self.name)

book1 = Product("0E345","BOOK","HAMIJATE NO GAL","Anime book with season 1 and 2")

print(book1)

#now lets make the new class poiting out that this class is a child of product

class Manga(Product):
    pass

#this will adopt all the process of the parent and we can instance a new object as before
manga = Manga("087GH","DVD","DINO DAIBOKEN","Season 1 dvd saga")

#since the parent has an override in the srt method, we will use the same
print(manga)

#now lets try to overwrite the methods from the parent to work as we want in a new class

class Movie(Product):
    distributor = ""
    producer = ""

    def __str__(self):
        return "Reference={},Name={},Producer={},Distributor={}".format(self.reference,self.name,self.producer,self.distributor)

#since the constructor from parent does not have the asignations, we need to make them ourselfs     
mazinkaizer = Movie ("084MZ","DVD","MAZINKAIZER","Mazinkaiser rise of the heroes")
mazinkaizer.producer = "Totem Productions"
mazinkaizer.distributor = "Seto Company"
#now with this we call the new str method just for this kind of object
print(mazinkaizer)

#lets create another movie type

mazinger_z = Movie ("034MZ","DVD","MAZINGER Z","Mazinger revenge of Kabuto")
mazinger_z.producer = "Totem Productions"
mazinger_z.distributor = "Seto Company"
#on this way we can now define many new objects that will be inherence from the main class known as parent class.
print(mazinger_z)