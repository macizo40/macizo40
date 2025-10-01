#lets start to practice inner objects which will help to use more the poo
#to start we need to think a set of objects that can be include in other objects and those need details

class Anime:

    def __init__(self,title,seasons,date_of_beginining):
        self.title = title
        self.seasons = seasons
        self.date_of_beginining = date_of_beginining
        print ("Anime record was created",self.title)

    #lets override the method str

    def __str__(self):
        return "{} ({})".format(self.title,self.date_of_beginining)
    
#lets now play with have our catalog of objects

class Catalog:
    #this will be a global value that can be managed in the entire class
    my_catalog = []

    #lets create his constructor, all class need one

    def __init__(self,catalog=[]):
        self.my_catalog = catalog

    #now lets create a method that will be saving our animes to that list
    def add_anime(self,anime):
        self.my_catalog.append(anime) 

   


dragon_quest = Anime("Daino Dai Boken",8,"11-11-2010")

print(dragon_quest)

#lets now use the append method to add the object anime to the catalog, this time we do not need to pass an argument 
#beacuse the calss has an inner variable so that it is initialized to empty already

cartoon_catalog = Catalog()

cartoon_catalog.add_anime(dragon_quest)

#lets print the object catalog

print(cartoon_catalog)


