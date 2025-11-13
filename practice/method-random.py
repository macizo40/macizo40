#we will continue with the method random to use data produced by the compiler
#we need to import the library
import random

#lets create 5 numbers in a for

for i in range(10): 
    print(f" we will create a random float number now:",random.random())


#you can notice that none of the numbers are greater than 1, so all are under 1 but not near to 0

for i in range(10): 
    print(f" we will create a random float number now:",random.uniform(1,10))

#this will create now numbers above 1 and less than 10, they they will be float too

for i in range(10): 
    print(f" we will create a random float number now:",random.randrange(10))

#this method will create random numbers, integers no decimals less than 10 and not including 0

for i in range(10): 
    print(f" we will create a random float number now:",random.randrange(0,101))

for i in range(10): 
    print(f" we will create a random float number now:",random.randrange(0,101,2)) #this will give you always pair numbers in the random

#the last numbers will tell you if the number is a multiple and that will be random

for i in range(10): 
    print(f" we will create a random float number now:",random.randrange(0,101,5)) #this will give numbers multiple of 5
