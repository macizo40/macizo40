#now lets work with the recurvise functions, python as other languages can manage this kind of calls

#here a simple decreate time watch

def counter(number):
    number -= 1
    if number > 0:
        print(number)
        counter(number)
    else:
        print("End of the counter")


#lest call the counter 

counter(100)

#one of the most commons usages is the facotrial of a number wich is the multiplication of the number minus 1, so the function will be

def factorial (number):
    if number > 1:
        number = number * factorial (number - 1)
    return number

#since the function is recursive 

print(factorial(5))


#now lets see a couple of functions that are common to convert some data as we saw in other languages 

#string to integer

n = int("10")

#string to float

f = float("1.3")

#the famous toString from java is the next one changing the value to be an string

t = str(10)

#this usually the methods will help to do several adecuations to avoid problems, lets see what is the result of something with no change

mixNumber = 10

mixText = "10"

#what is the result in python y if just do a '+'

print("doing a mixing operation ",mixNumber+int(mixText))

#the previous example do fail if you do not change the value to an int

#there are other types of methods as example change to binary a number

print("the binary of 10 is ", bin(10))

#other very usufel method in my opinion is the eval, which makes the python evaluate the content of the text and do the operation

print("doing some maths with eval:",eval("2+5"))

#we are passing a text which we know there is an operation there and the method will evaluate the action

#even eval can take some variables that are reported before the call and no need to special format them as f-string

outsiteVar = 10

print("doing an eval with an external value inside the text, the variable is {} and doing the eval now {} ".format(outsiteVar,eval("outsiteVar + 10")))

#other of the most common functions is the famous len this to ready the size of strings and list and more

print(len("this text will give me a value"))

