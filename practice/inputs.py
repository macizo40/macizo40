#lets continue practicing inputs in the python

#it is common that the inputs sometime does not cast to the right value that we want, as example lets say that we want a float 

myDecimal = input("Type a float number with a dot:")

print("Here is my decimal value from the input: {}".format(myDecimal))

#to play with getting many values from the input you can do a for with certaing range that will be number of values to enter

#lets use a list

myList =[]

for x in range(5):
    myList.append(input("Add the value number {} for the list: ".format(x+1)))


#now lets print my list and see all the values

print(" here is entire list: {} ".format(myList))