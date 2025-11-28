# we will take the same file that we did for the objects practice, but now we will be saving the data in the file.
#this practice was done before but the idea is to store the data of the objects in a file for persistent storage

#we need to import the open and pickle to manage the file
from io import open
import pickle

#with this class we will not do anything since is the object as is, we want the class tha store all the cakes
class Cake:

    #this like java we have a constructor method (called here init) that will assign the values recived in the call to their variables
    def __init__(self,name,flavour, size, form):
        self.flavour = flavour
        self.size = size
        self.form = form
        self.name = name

    #this method was new for me, this is a way to return to screen in format string=str the content of the object usually with print   
    def __str__(self):
        return 'Cake {} details are {} {} {}'.format(self.name,self.flavour,self.size,self.form)
    

#lest create a single method that will save some lines of code for each method
def empty_validation(self,value):
    if not self:
        print("No cakes available.")
        return None

    if value is None:
        print("No search value provided.")
        return None


#here is where we will play with the pickle file, for this time the init should be always opening the pickle file 

class CakeShop:

    cakes_list =[] #this will now have the whole list of the cake.

    #the constructor will change since we want to first load 
    def __init__(self):
        self.load_file()

    def __str__(self):
        return "This is the Cake Shop class object"
    
    def add_cake(self,cake):
        self.cakes_list.append(cake)
        self.save_file()
    
    def load_file(self):
        #we will use now the advanced method to open in binary and with read rights too
        my_shop_file = open('practice/files/my_shop_file.pckl','ab+')
        #since the append method set the pointer at the end, we do set it always to the begining.
        my_shop_file.seek(0)
        #now the first time could not be there, it will give error, we need to try and catch any issue in the real world.
        try:
            self.cakes_list = pickle.load(my_shop_file) #first time does not exist and will pass to the next block
        except: 
            print("File is empty or is the first time that is created")
        finally:
            my_shop_file.close() #in case that error we always close it
            print("We have loaded {} objects from the file".format(len(self.cakes_list)))
    
    def save_file(self):
        #this save file process will be used to replace all the content of the file always.
        my_shop_file = open('practice/files/my_shop_file.pckl','wb')
        pickle.dump(self.cakes_list,my_shop_file)
        my_shop_file.close()

    #image then what I want to know from an object, maybe his form, we need a method to get it, we will use any value
    def show_cake(self, value=None):
        
        empty_validation (self,value)

        # Normalize value for case-insensitive comparison
        search_value = str(value).lower()

        for cake in self.cakes_list:
            # Dynamically check attributes
            for attr in ("name", "flavour", "size", "form"):
                attr_value = getattr(cake, attr, None)
                if attr_value is not None and str(attr_value).lower() == search_value:
                    print(f"Match found by {attr}: {cake}") #this will calls the str method that we set in the constructor
                    return cake

        print(f"No cake found matching '{value}'.")
        return None

    #now lets try the same approach as before to remove from the list an object 

    def remove_cake (self, value=None):
        #same as before we do validate the input
        empty_validation (self,value)

        # Normalize value for case-insensitive comparison
        search_value = str(value).lower()

        #this will create a variable of the position and the object too, this will be always the first value

        for i,cake in enumerate(self.cakes_list): 
            # Dynamically check attributes
            for attr in ("name", "flavour", "size", "form"):
                attr_value = getattr(cake, attr, None)
                if attr_value is not None and str(attr_value).lower() == search_value:
                    del(self.cakes[i])
                    print(f"Found by {attr}: {cake} in position {i}, deleting.....")
                    return cake

        print(f"No cake found matching to delete '{value}'.")
        return None


#now we can play with some characteristics of the cakes
red_velvet = Cake ("red velvet","Chocolat","Big","Square")
addiction = Cake ("addiction","Strawberry","Big","Circle")
carrot = Cake ("carrot special","Carrot","Big","Triangle")

#now lets use the __STR__ method by just send to print the object, this will automatically use the __str__ method
print(red_velvet)
print(addiction)
print(carrot)


#now again lest create the class cake shop and sent the obejcts type cake

cake_shop = CakeShop()

cake_shop.add_cake(red_velvet)
cake_shop.add_cake(addiction)

cake_shop.show_cake(red_velvet.flavour)


