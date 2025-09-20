#lets practice another way to create classes and the way tha atributes may be there and not need to have a constructor

#this will create the class and you can see there is not constructor
class HotDogs:
    pass


#creating the object no attributes
hot_dog = HotDogs()

#now lets add some attrbites that are not defined in the class

hot_dog.size = "Jumbo"
hot_dog.flavour = "ChiliDog"

#lets print the attributes

#since we want to concanate the exit, we may skip either f-string or format, beacuse we want them at the end always 
print("The size is",hot_dog.size)
print("The flavour is",hot_dog.flavour)

