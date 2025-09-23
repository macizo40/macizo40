#lets practice another way to create classes and the way tha atributes may be there and not need to have a constructor

#now lest test and play more with the obejct and instance of them, aslo how to change values that are inside the class
class HotDogs:
    mayo = False

    def __init__(self):
        print("We jus have a new hot-dog")
    
    def add_mayo (self):
        self.mayo = True
    
    def with_mayo(self):
        if (self.mayo):
            print("I am a hot dog with mayo")
        else:
            print("I am a hot dog with no mayo")

    
#creating the object no attributes
hot_dog = HotDogs()

#now lets add some attrbites that are not defined in the class

hot_dog.size = "Jumbo"
hot_dog.flavour = "ChiliDog"

#lets print the attributes

#since we want to concanate the exit, we may skip either f-string or format, beacuse we want them at the end always 
print("The size is",hot_dog.size)
print("The flavour is",hot_dog.flavour)

#now lets try the methods that we have defined in the class

hot_dog.with_mayo()

#now lets modify the propoerty that add the mayo to the hot dog

hot_dog.add_mayo()

#now let see how the obejct does respond after the method

hot_dog.with_mayo()

