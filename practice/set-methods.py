#now lets take a look to the methods that the type set does have

my_set = set()

my_set.add(1)
my_set.add(2)
my_set.add(3)

print(my_set)

#you can remove an item with discard

my_set.discard(2)

print(my_set)

my_set.add(2)

print("now the value is",my_set)

my_set.add(5)

print("now the value is",my_set)

#since the collections are linked to reference there are methods to copy one set to another set, leaving the original untouch 

my_set_copy = my_set.copy()

my_set_copy.discard(5)

print(f"now the original set have {my_set} and the copy have {my_set_copy}")

#and it has it's own clear method

my_set.clear()

print(my_set,"is empty")

#lets bring values to the original

my_set = my_set_copy.copy()

print("I have now values",my_set)

#now we should be doing something more complex with the sets, as in maths we can see join, part of or contains some other, this is data

my_first_set = {1,2,3}
my_second_set = {3,4,5}
my_third_set = {0,1000}
my_fourth_set = {1,2,3,4,5}
my_last_set = {5,6}

#as we did in our school we can take those sets to compare each other and have an universe in this case any intersection

print("is the set {} disjoin from {} {}".format(my_first_set,my_third_set,my_first_set.isdisjoint(my_third_set)))
#this will give false because there is yes an intersection 
print("is the set {} disjoin from {} {}".format(my_first_set,my_second_set,my_first_set.isdisjoint(my_second_set)))

#now lets see if a set is part of another set, lets called subset, it should contains all the elements
print("is the set {} subset of {} {}".format(my_first_set,my_fourth_set,my_first_set.issubset(my_fourth_set)))
#this will give false, beacuse to be a subset, all the items must exist in the bigger set
print("is the set {} subset of {} {}".format(my_last_set,my_fourth_set,my_last_set.issubset(my_fourth_set)))

#another method is the super set, which is vicesersa, now lets see if the bigger does contains the small ones

print("is the superset {} of {} {}".format(my_fourth_set,my_second_set,my_fourth_set.issuperset(my_second_set)))

#also for the first set

print("is the superset {} of {} {}".format(my_fourth_set,my_first_set,my_fourth_set.issuperset(my_first_set)))






