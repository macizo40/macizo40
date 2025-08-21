#lets start using more the return values from the functions that we are creating, now lets use some list

def list_return():
    return [1,2,3,4,5]

print (list_return())

#to that return we can do some slicing stuffs like point to the current last location

print(list_return()[-1])

#another use of the slicing 

print (list_return()[2:4])

#strong usage of return values is that the functions can return many values different as exmaple

def multiple_values():
    return "my text",20,list_return()

#now that you know the order you can assign no matter the values to an external varibale like

myText,myNumber,myList = multiple_values()

print("first variable is {} second is {} and third is {}".format(myText,myNumber,myList))


#now lets start to passing values to the functions, this values can be the same in the method and you do not need to assign them

def math_sum(a,b):
    return a+b

print(f"the total is {math_sum(2,3)}")

#this was a simple value return that will help us to define the math, but now lets assign in the moment values to the function

print(f"the values will be the same but we set the order {math_sum(b=3,a=6)}")

#most common errors are to pass values that may be empty so to validate this you can always check before start any operation

def two_values(a=None,b=None):

    if a==None or b==None:
        print("one or more values can not be null")
    else:
        print(f"result is {a-b}")
    

#lets call the method with no values to check the message

two_values()

#now with just one value

two_values(2)

#now lets try the math

two_values(4,2)
    
    
