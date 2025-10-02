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

    def __str__(self):
        for item in self.my_catalog:
            print(item.title)
        return "EOL"
    
    #image then what I want to know from an object, maybe his form, we need a method to get it, we will use any value
    def get_info(self, value=None):
        
        # Normalize value for case-insensitive comparison
        search_value = str(value).lower()

        for item in self.my_catalog:
            # Dynamically check attributes
            for attr in ("title","seasons","date_of_beginining"):
                attr_value = getattr(item, attr, None)
                if attr_value is not None and str(attr_value).lower() == search_value:
                    print(f"Match found by {attr}: {item}") #this will calls the str method that we set in the constructor
                    return item

        print(f"No anime found matching '{value}'.")
        return None


   


dragon_quest = Anime("Daino Dai Boken",8,"11-11-2010")

print(dragon_quest)

#lets now use the append method to add the object anime to the catalog, this time we do not need to pass an argument 
#beacuse the calss has an inner variable so that it is initialized to empty already

cartoon_catalog = Catalog()

cartoon_catalog.add_anime(dragon_quest)

#lets print the object catalog

print(cartoon_catalog)

cartoon_catalog.get_info(dragon_quest.title)

saint_seiya = Anime("Saint Seiya",9,"12-12-1996")

cartoon_catalog.add_anime(saint_seiya)

print(cartoon_catalog)


