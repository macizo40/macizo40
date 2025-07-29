#testing the current values that a tupla does have 

tupla = (234,"text",[2,2,3,4,5,6],-50)

print("Values of the tupla are:{}".format(tupla))

#all values are inmutable so there is no way to change it, as every list you can do slicing on the values

print("from the second value to the last {}".format(tupla[2:]))

#like a matrxi we can access to the elements in any list type inside the tupla,

print("element inside the list inside the tupla this should be a 4={}".format(tupla [2][3]))

#you can use any other auxiliar command to see the lenght of the tupla or the values that it has

print("lenght of the tuple is {} and the lenght of the list inside the tupla is {} ".format(len(tupla),len(tupla[2])))

#to do some belongs test and delete duplicated values you can use the groups

group = set()

print("this is a group that is empty {}".format(group))

#now we can create a set that will be having some values 

group = {1,2,3}

print("now the group does have values {}".format(group))

#now we will ve use the method add to put another element a the end of the group

group.add(4)

print("now there is a new value in the group {}".format(group))

#in the pas the group added at the end, but thi kind of group does set all the values in disorder, so let's add a new value minor the current ones

group.add(0)

print("now lets see that the vale is at the begining since is the 0 so here is the group {}".format(group))

#the same will be for any other kind of value, can be letters too, so they will be in the add but there is not specific order

group.add('h')
group.add(2.1)
group.add("hello")

print("now lets see where the letter/float/word are is in this group {}".format(group))

#now there are validtions that will help to understand if a value does exist in a group

people = {'hector','mario','leon','miguel'}

if 'dainer' in people:
    print("yes the person does exist in the group")
else:
    print("person does not exist in the group")

#we can use the not before to just make the condition negative

if 'mario' not in people:
    print("not in the group")
else:
    print("yes exist")

# now there is time to use the groups to remove all duplicated data, on this case we can have a single list that we will move to a group

duplicated = [1,2,1,2,1,3,0,4,5,5,6,6,8,4,43,3,4,3,3,44,3,4]

print("this is the list with all values {}".format(duplicated))

#now lets cast the values to a set this is the easy way to reduce data from a huge list

nondup  = set(duplicated)

print("now this is the list with no mode duplicated data {}".format(nondup))


# now for practice methods and make sure that a list does remove the duplicated data but still does have the propoerties as a list

duplicated = list(set(duplicated))

print("now the list still is a list but with no duplicated data {}".format(duplicated))

#now lets try to avoid some usage of variables to just print the information

print("now we will print just the list with no duplciated data here {} not using a variable to cast it".format(list(set(duplicated))))


# to end there is a way to use the elements in the list as the trigger for a loop and add them to an specific list 

mylist = {"one", "five", "three", "six"}

for user in ["nine", "ten", "eleven", "zero", "two"]:
    mylist.add(user)
 
for user in ["one", "five", "six"]:
    mylist.remove(user)

print("now the list is {}".format(mylist))



