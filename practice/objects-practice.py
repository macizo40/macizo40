#lets do some new test about the objects 
#a class is a template of objects that have some similar attributes

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
    
#now we can play with some characteristics of the cakes
red_velvet = Cake ("red velvet","Chocolat","Big","Square")
addiction = Cake ("addiction","Strawberry","Big","Circle")
carrot = Cake ("carrot special","Carrot","Big","Triangle")

#lest create a single method that will save some lines of code for each method
def empty_validation(self,value):
    if not self.cakes:
        print("No cakes available.")
        return None

    if value is None:
        print("No search value provided.")
        return None


#now lets use the __STR__ method by just send to print the object, this will automatically use the __str__ method
print(red_velvet)
print(addiction)
print(carrot)

#now what can we do with the object in a cake store, first we need the class name 

class CakeShop:

    #same logic as before, lets get a list of objects that will be our constructor, it will get a list of cakes objects
    def __init__(self,cakes=[]):
        self.cakes = cakes

    def __str__(self):
        return "This is the Cake Shop class object"
    

    #image then what I want to know from an object, maybe his form, we need a method to get it, we will use any value
    def show_cake(self, value=None):
        
        empty_validation (self,value)

        # Normalize value for case-insensitive comparison
        search_value = str(value).lower()

        for cake in self.cakes:
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

        for i,cake in enumerate(self.cakes): 
            # Dynamically check attributes
            for attr in ("name", "flavour", "size", "form"):
                attr_value = getattr(cake, attr, None)
                if attr_value is not None and str(attr_value).lower() == search_value:
                    del(self.cakes[i])
                    print(f"Found by {attr}: {cake} in position {i}, deleting.....")
                    return cake

        print(f"No cake found matching to delete '{value}'.")
        return None

#now again lest create the class cake shop and sent the obejcts type cake

cake_shop = CakeShop(cakes=[red_velvet,addiction,carrot])

#after the class is create we can now start using the methos inside the class

cake_shop.show_cake(addiction.flavour)
cake_shop.show_cake(carrot.flavour)

#lets use a different value to find

cake_shop.show_cake(addiction.form)

#lets try the empty value to see if the method works different

cake_shop.show_cake()

#now les try a value that we know that does not exist at all

cake_shop.show_cake("simple")
#lets try to send a wrong value first
cake_shop.remove_cake("simple")

#now lets try to delete red_velvet
cake_shop.remove_cake(red_velvet.flavour)
#checking that was removed from the list
cake_shop.show_cake(red_velvet.flavour)
#now lets try to find it with name
cake_shop.show_cake(red_velvet.name)
#now lets try to remove an already removed cake
cake_shop.remove_cake(red_velvet.name)
