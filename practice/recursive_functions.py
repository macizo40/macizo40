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
