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
