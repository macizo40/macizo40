#now lets see also with dictionaries some special methods that will help us more

my_dict = {"a":"alpha","b":"beta","c":"charlie","d":"delta","e":"echo","f":"foxtrot"}

print(f"the code for the letter a is {my_dict['a']}")

#adding the second value is by default a message if key does not exist
print(f"the code for the letter z is {my_dict.get('z','not found')}") 

#there is a way to validate if the key does exist is using the next format
print(f"does the z exist in the dictionary = {'z' in my_dict}")

#now one that yes does exist
print(f"does the z exist in the dictionary = {'f' in my_dict}")

#there is a general way to get all the keys
print(f"all tje keys in the dictionary are:{my_dict.keys()}")

#also there is a method to get all the values
print(f"the values of the dictionary are:{my_dict.values()}")

#finally to get all keys and values we use items
print(f"all the items in the dictionary are:{my_dict.items()}")

#a regular form to iterate the content of a dictionary is with a for loop poiting to values and keys
for i in my_dict:
    print(my_dict[i])
    print(i)
print("-----")
#lets give the use in case that we want to show keys
for i in my_dict.keys(): #this method will iterate and give to i each key in the loop, you save a line of assignation
    print(i)
print("-----")
#now let give only values to the iteration variable i
for i in my_dict.values(): #this method will iterate and give to i each key in the loop, you save a line of assignation
    print(i)
print("-----")
#now lets use the multi variable in the for to give to two iteration variables the keys and the values from items that returns two values
for key,value in my_dict.items():
    print(f"a key is {key} and his value is {value}")
print("-----")

#a method that is shared with other collections is the 'pop' which will extract and remove the item from the dict

print(my_dict.pop('f','not found')) #we can play adding a text by default

print(f"lets see now the items after the pop: {my_dict.items()}")

#if we try to pop a value that does not exist 

print(f"I want to pop a value z for zulu:{my_dict.pop('z','not found')}")

#finally also it share the clear method to empty all the dictionary

print(f"time to clear all the dictionary {my_dict.clear()}")

