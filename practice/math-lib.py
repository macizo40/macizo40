#lets start with the math library to do some very cool calculations 

#we have to import math

import math

pi = 3.141656

print(f"we will use simple round method for {pi} that is {round(pi)}")
print(f"but if we want to round up lets use 3.5 a different result is {round(3.5)}, it round up")

#but now lets start using more math methods this like other to round down

print(f"using the methid 'math.floor' on pi will give {math.floor(pi)}") #all items not matter what will round down

#meanwhile the floor downs, the method ceil is always going up if have any decimal in the number

print(f"lets move up the number {pi} to ceil is {math.ceil(pi)}")

#the math methods more commons are the absolute number, it does not matter if is positvie or negative it removes the sing

print("the absolute value of -10 is ",abs(-10))

#we do have some values as sum to get the total of all values even in a list

my_numbers = [3,3,3,3,3]

print(f"total of values in {my_numbers} is {sum(my_numbers)}")

#if we want that values even includes floats we can use fsum

print(f"float format of the total from {my_numbers} is {math.fsum(my_numbers)}")

#there was an issue with sum in some versions before we will check this

my_floats = [0.999999,1,2,3]

print(f"using the regular sum with floast {my_floats} the result is {sum(my_floats)}")

print(f"checking that gives the same result with math lib is {math.fsum(my_floats)}")

#math trunc is for more the methiod that will not make any round and will remove the decimals

print(f"we will trunc the sum of the floats from {math.fsum(my_floats)} to {math.trunc(math.fsum(my_floats))}")

#we can use specific methods for pow and sqrt

print(f"using pow 2 elevate to 3 is {math.pow(2,3)}")

print(f"now the square root of 8 is {math.sqrt(8)}")

#to avois using manual inputs for constants we can use the ones that are part the lib

print("the value of pi using math.pi is ",math.pi)

print("the value of the constant e using math.e is ",math.e)
