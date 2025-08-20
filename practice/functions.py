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

#there are some others practives as we can do a loop with some values to do a repeteable action like print the 5 plus any number

def loopPrint_number_5():
    for iteratorNumber in range(10):
        print("5 * {} = {}".format(iteratorNumber,iteratorNumber*5))

loopPrint_number_5()

#now lets do it more dynamic since we are always doing the number 5, now we will do it to do the same with any number that we pass

def math_table_any_number(number):
    for iterator in range(10):
        print("{} * {} = {}".format(number,iterator,number*iterator))

#now lets called with the number that we pass, let's do it for the number 1 and 2

math_table_any_number(1)
math_table_any_number(2)

#the previous example did start with 0 and ends with 9 since the values are starting as elements of an array, so let's try to fix that now

def math_fixed_table(number):
    for multiplier in range(11):
        if multiplier != 0:
            print("{} * {} = {}".format(number,multiplier,number*multiplier))


math_fixed_table(3)
math_fixed_table(4)

#using the values of the if will be part of the math operation

#lets start using another concept about the functions is to local variable or global variable
#same as other OO languages, the local variables just exist in the method and not visible to the rest of the code

def printing_local():
    localText = "I am a local variable"
    print(localText)

#now lets call the method just to see how it works
printing_local()

#now let's try to print the variable localText ouside the method
# print(localText) this line gives NameError: name 'localText' is not defined

#now let's use the a varialbe outside the method and try to print it inside a method

globalText = "I am a global text"


def print_global():
    print(globalText)

print_global()

#now lets try to modify global variables inside methods or functions

#taking the previous text let's override the value inside the method


print(f"this is hte value before the method = {globalText}")

#define a new method to change the value inside, but you need to use a variable with a same name, this is a new varible visible only in the method

def change_value():
    globalText = "Changed on the method"
    return globalText

globalText = change_value()

print(f"this is hte value after the method = {globalText}")

# another easy way is just to return values with no variables use

def simple_return():
    return "my simple return text"

globalText = simple_return()

print(f"this is hte value using the simple return method = {globalText}")