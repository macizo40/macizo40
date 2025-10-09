#lets now practice as java to pass methods and attributes from a parent class to child class

class Product:

    def __init__(self,reference,type,name,description,producer=None,distributor=None):
        self.reference = reference
        self.name = name
        self.type = type
        self.description = description
        self.producer = producer
        self.distributor = distributor

    def __str__(self):
        return "Reference={},Name={}".format(self.reference,self.name)
    

manga = Product("0E345","BOOK","HAMIJATE NO GAL","Anime book with season 1 and 2")

