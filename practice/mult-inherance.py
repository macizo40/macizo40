#this new module we will review the concept of multi inherence from different classes

#lets create small classes to see how the methods and variables that are same in two or more classes are read by the child class

class One:
    def __init__(self):
        print("Class one here")

    def a(self):
        print("I do provide this method a to my child")


#lets create a second class with his constructor

class Two:
    def __init__(self):
        print("Class two here")

    def b(self):
        print("I do provide this method b to my child")


#now lets play with the multi inherance from one and two 

class Three (One,Two):
    pass

#now lets see when there are two or more same methods/propoerties, it will take the frist to find from left to right
#by creating the object lets see that constructor from class one is called 

obj1 = Three()

#this will use  a different order and lets see that constructor from class two is called
class Four(Two,One):
    pass

obj2 = Four()

#lets call the methods that all inherence provides

obj1.a()
obj2.b()


