#this is a quick topic and show how to create private methods and attributes in the class, something that is not regular used in python

class Private:

    #starting with underscore like a special method I can create new attributes 

    __my_private_attr = "I am private attribute"

    #same for he method 
    
    def __my_private_method():
        print("I am private method")

#now lets try to access them as regularly we do

myObject = Private()

#this will give an error in the runtime
myObject.__my_private_method()
