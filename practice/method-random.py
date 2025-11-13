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

#random not only do choose from numbers, in any case that we have an string we can try to select a random letter from it

mystring= "I am string and I have letters"
for i in range(10):
    print("from the string we select:",random.choice(mystring)) #yes spaces in the string are also considered

#but now lets do it with some list and values in the list like names

mylist = ["Pable","Tom","Rocco","Jean","Peter","Hannah"]

for i in range(6):
    print("random name from the list:",random.choice(mylist))

#in anothers method are also the method to change the order of the values in the list, again is for reference so anything will be changed

print(f"my original list is {mylist} but then I will shuffle and the new value is {random.shuffle(mylist)} again  {mylist}")

#another method is sample which will take elements from the list you can define how many

print("here is 2 samples from the list:",random.sample(mylist,2))

#lets play with a for to do 1 to 4 sample

for i in range(4):
    if i > 0:
        print(f"a sample number is {1} then will be {random.sample(mylist,i)}")
