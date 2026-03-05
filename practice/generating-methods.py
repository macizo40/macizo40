#there has been different paths to generate values, now we will use some of the generated methods that will help us 

#this time we will see the function "yield" instead of return to see how it changes the way to use the value in a method.

def get_pairs(value):
    for numbers in range (value+1):
        if numbers%2 == 0:
            yield numbers


#this time instead of filling a huge list, we know that numbers is an object that will contains only pairs numbers by default

print("here is the object that we find",get_pairs(10))

#know that we know is an object that contains pairs numbers we can use them like this:

for n in get_pairs(100): #this is an object that contains elements depending the number of elements the methiod will run
    print(n)

#now is we store this element in an object we will see how to iterate it since it is in the memory

my_yield_numbers = get_pairs(6)

print(next(my_yield_numbers))

print(next(my_yield_numbers))

print(next(my_yield_numbers))

print(next(my_yield_numbers))
