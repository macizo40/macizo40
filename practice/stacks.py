#there are not any specific type of stack in python but we can simulate them with the list

# we will play with the list to give it the Last in, First Out or First In, Last Out

#lets create the empty stack

myStack=[]

print("my stack is {}".format(myStack))

#lets then start to append and follow the proccess of first in is the last out

myStack.append('first')
myStack.append('second')
myStack.append('third')
myStack.append('fourth')

print("the stack now will show the first at the end of the list which means the first that went in {}".format(myStack))

#now lets use the pop method in the list that will simulate taking the last value added removed from the list
#the method pop can also find an specific value but to simulate the pop is just the last one in the list.
#we will save the value of the pop to do not loss it and print it

valueOut = myStack.pop()

print("the value that was out is {} and then my stack just leave {}".format(valueOut,myStack))

#now lets add another value to see that is at the end and if we do another pop that is the first to out

myStack.append('fith')

print("adding a new value fith and now the stack is {}".format(myStack))

myStack.pop()

print("now after the pop, the last value added is now out the stack {}".format(myStack))


#we can also play with que that is firt in and first out. for this you need to import the library

from collections import deque

#here we are creating a que that is empty

myQue = deque()

print("now will play with que here {}".format(myQue))

#now we will play with it to confirm that the first that is in will be the first that will be out

myQue.append('first')
myQue.append('second')
myQue.append('third')

print("lets see how the order is now in {}".format(myQue))

#as stack has a method called pop that takes the last of the list there is a method for que that pop but from the begining in the left.

valueOutLeft = myQue.popleft()

print("now lets check the value of the {} and the element take out was {}".format(myQue,valueOutLeft))

#as we can see que model is working most to control the access or the order of request.