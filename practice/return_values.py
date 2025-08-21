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
