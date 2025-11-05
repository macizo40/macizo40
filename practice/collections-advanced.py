#we will work again with collections but here will be an advanced level now we need to import 

#counter will transform the content in a dictionary 
from collections import Counter

myNumberList = [1,2,3,4,1,2,3,4,5,6]

print(f"the values that were found are {Counter(myNumberList)}, where the first number is the value and second is the times found")

#we can use also counter with a string which can be 

myString = "Hello this is my string and can be used in counter"

print("Here is the letters and their times in the string {}".format(Counter(myString)))

#the previous ones is a general method that may not be valuable since letters are many

#having example a list of words
myWordsList = "dog cat cat cat cat dog horse bird dog cat "

#using the method split we can transform each work into a list

print(f"here is the list after an split {myWordsList.split()}")

#now in a list we can count the times that the word does appear

print("here is the list counter after split {}".format(Counter(myWordsList.split())))

# we can now save this values to a counter value, so lets compare two list to see if they have the same number of times the words

mySecondWordList = "dog cat cat cat cat dog horse bird dog cat "

counter1 = Counter(myWordsList.split())
counter2 = Counter(mySecondWordList.split())

print(f"here is my counter 1 {counter1} and here my counter 2 {counter2}")

#this validation will compare the dictionaries are same, giving that both does have the same number of elements and the same times
if counter1 == counter2:
    print("both counter has the same number of times the sames words")

#now there are some methods for counters that van help to give the most common values 

print(f"the most common element is {counter1.most_common(1)}") #using a number 1 gives only higher most common

print(f"the two most common values are: {counter1.most_common(2)}") # this will be the first and second

print(f"this is the whole list of values, from the higher to the lower: {counter1.most_common()}") #no number 

#lets use now numbers

counter3 = Counter(myNumberList)

print (" count the list of numbers: {}".format(counter3))

#we can see all the items

print("the items are: ",counter3.items())

print("the keys are: ",counter3.keys())

print("the values of each key are: ",counter3.values())

print("we want to know how many elements are in the list we can use a sum() like:",sum(counter3.values()))

print("we can get it back to cast(trasform) the counter again in a list but this are not repeated values:",list(counter3))

print("we can also cast back to a dictionary:",dict(counter3))


#############################################################################################