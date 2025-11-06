#lets have more practice with the dictionaries and how they can be accesed 

mydictionary = {}

#regularry when any element does not exist in the dict will give you error like

#print("this element does not exist:",mydictionary['a'])

#now we will use the package defaultdict to avoid have values nulls

from collections import defaultdict

#at this point we will have elements like float 
mydictionary = defaultdict(float)

print("we can see the elements of the dict now:",mydictionary)

#when we try to access to one element that does no exist we see a different behaviour 

print("this element does not exist in the defaultdict:",mydictionary['b'],mydictionary) #but this got added even is does not exist

#we can do also with strings and it wil get assigned a default value

d2 = defaultdict(str)

print("here is the default value now added:", d2["save"],d2)

#another part of the regular dict is that the order of the values is not the same that was added 

d3 = {}
d3['dos'] = 'two'
d3['uno'] = 'one'
d3['tres'] = 'three'

#if you added in disorder they will remain as is

print("the dict will not respect the order:",d3)

#but we can use the ordered type to even they got in disorder they get oredered

from collections import OrderedDict

d4 = OrderedDict()
d4['dos'] = 'two'
d4['uno'] = 'one'
d4['tres'] = 'three'

print("the dict will respect the order:",d4)

#lets see some advanced methods with tuples

t = (20,60,60)

#to access to any element we use the idex location

print("this is the first element: ",t[0])

#lets use the collections called named tuple, this is inmutable (no changed) and can be used as a small class

from collections import namedtuple

People = namedtuple('People','name lastname age')
#this will created a single people which is an inmutable object 
people = People(name='Me',lastname='Too',age=23)

#now we can access the data like this:

print(f"the object {people} does have this info: {people.name}, {people.lastname} and {people.age}")

#another way to use this namedtuple is to also go for locations like this:

print(f"now we will use the location so the data is {people[0]}, {people[1]} and {people[-1]} as the last element")
