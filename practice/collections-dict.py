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
