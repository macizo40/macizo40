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


class Dell(Computer):
    pass

class HP(Computer):
    extra_device = ""
    hard_disk_type = ""

    def __str__(self):
        return "brand={},Name={},Producer={},Distributor={}".format(self.brand,self.name,self.extra_device,self.hard_disk_type)

