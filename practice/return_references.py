#lets see this example we will pass a simpe value and the value will not change

def passValue(number):
    number-1


#create a single variable that will not change since function will do a copy

myValue=5
print(f"the original value is {myValue} and after the method is {passValue(myValue)}")

#the previous code will display the original value is 5 and after the method is None, because number is just local and is not returned

#now lets start doing more passing values as know by reference, this is focus to certain types of variables like the list
#which in this case there will be not a copy and the orignal values will be changed
myList = [100,12,500]
print(f"this is the original list {myList}")
def myListChanged(numbers):
    for i,n in enumerate(numbers):
        print(f"working with i={i} and n={n}")
        numbers[i] *= 2

#lets run the  method
myListChanged(myList)

#lets print again the value

print(f"this is the list after the method {myList}")

#even in the method there was a new variable, the list type dos gets affected since thinks as a reference, this will happen with list

#now to avoid that a reference does affect and original list, we can do the next, anytime that we do an slicing it is created a copy
#this will not affect the original value

def avoidReference(numbers):
    for i,n in enumerate(numbers):
        print(f"working with i={i} and n={n}")
        numbers[i] *= 2

#lets create a new list 

myNotChangedList = [1,2,3,4,5]

print(f"this is the original list {myNotChangedList}")

#now the trick is to do an slicing at the moment to call the method and this will create a copy and not a reference

avoidReference(myNotChangedList[:])

print(f"this is the list after the method {myNotChangedList}")
