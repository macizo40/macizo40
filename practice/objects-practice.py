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
carrot = Cake ("carrot","Carrot","Big","Triangle")



#now lets use the __STR__ method:
print(red_velvet)
print(addiction)
print(carrot)

#now what can we do with the object in a cake store, first we need the class name 

class CakeShop:

    #same logic as before, lets get a list of objects that will be our constructor, it will get a list of cakes objects
    def __init__(self,cakes=[]):
        self.cakes = cakes

    #image then what I want to know from an object, maybe his form, we need a method to get it, we will use any value
    def show_cake(self, value=None):
        if not self.cakes:
            print("No cakes available.")
            return None

        if value is None:
            print("No search value provided.")
            return None

        # Normalize value for case-insensitive comparison
        search_value = str(value).lower()

        for cake in self.cakes:
            # Dynamically check attributes
                for attr in ("name", "flavour", "size", "form"):
                    attr_value = getattr(cake, attr, None)
                    if attr_value is not None and str(attr_value).lower() == search_value:
                        print(f"Match found by {attr}: {cake}")
                    return cake

        print(f"No client found matching '{value}'.")
        return None   
