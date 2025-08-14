#lets start playing more with the functions or methods as other languages does work
#using a simple word def you start to define all the methods and functions that you want

def sayHello():
    print("I just want to say hello")


#now we are ready to call this function or method all the time that we want 

sayHello()

#we can play with a function that always print the value of an element any to avoid been typing always some text
def printAlways(object):
    print(f"this is the value of the element {object}")

#the object is any type of value, anything, this is a object oriented so anything can pass and anything can be print
printAlways("one")
printAlways(3)
printAlways(True)

#lets print a dictionary

myDictionary = {'one':'uno','two':'dos'}

printAlways(myDictionary)

#lets play no with f-string now back to format, playing here we can pass objects and print them in the order

def myOrderedList(obj1,obj2,obj3):
    print("this is the firs element {}, now the second {} and finally the third {}".format(obj1,obj2,obj3))

myOrderedList("one",2,True)

#what can happen if we do not pass all the elements, it fails, you need to pass all the elements defined
