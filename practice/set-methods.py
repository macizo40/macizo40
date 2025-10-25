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


#now with a more advanced methods we can do unions, update and more with the sets just like math

#union in a new set

my_union_set = my_first_set.union(my_second_set)

print(f"now the new set is {my_union_set} and lets see that other sets are not touched {my_first_set} and {my_second_set}")

#in nay case that you want to update with an union an specific set, you need to use update

my_first_set.update(my_second_set)

print(f"now we can see that new set is {my_first_set} just like the union {my_union_set} but the second set no changes {my_second_set}")

#now to save the difference in a new set from the original

my_difference_set = my_second_set.difference(my_last_set)

print(f"now the difference is stored here {my_difference_set} from the original {my_second_set} and {my_last_set}")

#now lest update one of the set with the difference from the original

my_second_set.difference_update(my_last_set)

print(f"now the new value of the set is {my_second_set} and the other stay as original {my_last_set}")

#lets now create and get the values of intersection, are those values that are equal in two sets

my_intersection = my_fourth_set.intersection(my_last_set)

print(f"now the intersection is {my_intersection} ")

#we can also update them too

my_last_set.intersection_update(my_fourth_set)

print(f"now last set will have only the values of intersection {my_last_set} and the other will be {my_fourth_set}")

#finally there is a method that will take the different values and not the ones that are repeated vicesersa of intersecction

my_simetric_difference = my_fourth_set.symmetric_difference(my_second_set)

print(f"finally to have the value {my_simetric_difference} from {my_fourth_set} and {my_second_set}")





