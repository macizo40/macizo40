#on this time we will work with the concep polymorphims to make sure understand the different ways to inherance in classes

#les take as previous example some parent class and create child classes 

class Computer:

    def __init__(self,brand,type,name,description):
        self.brand = brand
        self.name = name
        self.type = type
        self.description = description
        
    def __str__(self):
        return "brand={},Name={}".format(self.brand,self.name)


class Acer(Computer):
    pass

class HP(Computer):
    extra_device = ""
    hard_disk_type = ""

    def __str__(self):
        return "brand={},Name={},Producer={},Distributor={}".format(self.brand,self.name,self.extra_device,self.hard_disk_type)


#lets create some objects to test the str method


aspire = Acer("Acer","Desktop","Aspire","Desktop computer with speakers")

print(aspire)

#now lest inherance from a subclass no the parent

class Sony(HP):
    def __init__(self,brand,type,name,description,extra_device,hard_disk_type):
        self.brand = brand
        self.name = name
        self.type = type
        self.description = description
        self.extra_device = extra_device
        self.hard_disk_type = hard_disk_type

vaio = Sony("Sony","Laptop","VAIO","Laptop with burner included","card reader","solid")

print("this object has the same values as his parent, but it is empty",vaio.extra_device)

#lets now create a list of the objects

computers = [aspire,vaio]

#now that those are in the list does not matter, we read each with a for loop

for comp in computers:
    print(comp,"\n") #this will call each str method of each object

#after the run you will see different behaviours of the print since each does have their method and others does use the parent method