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

#now lets continue playing with the format that some strings does have,using format but when we want to add more we can play like this

#lets insert 30 spaces before the text

print("{:>30} this text is after 30 spaces".format("aligned"))

#the previous exmaple is considering align it to the right, so what if need to align to the left like this :

print("{:30}".format("leftAligned"))

# the previous exmaple does not aligned to left, is just creating 30 spaces after the text

#now we can play to set the text in middle like 30 spaces, but there will be 15 before and 15 after

print("{:^30}".format("center"))