#now lets see the most commons methods to handle lists

my_initial_list = [1,2,3,4,5,6]
my_list_to_count = [1,1,1,1,1,'hola','hola','a','a','a']

my_list_to_sort = [1,0,7,3,9,10,455,2,1000]

#methods to add at the end
my_initial_list.append(7)

print(my_initial_list)

my_second_list = my_initial_list

my_second_list.append(8)

print(my_second_list)
#remember that the list are references so, any change in the second list will be the same on the first 
print("Initial list content:",my_initial_list," the second list content:",my_second_list) 

#now let's use some methods to clear the list
my_second_list.clear()

#since is a reference then the clear affects to the original list
print("Initial list content:",my_initial_list," the second list content:",my_second_list) 

#methods to join two list, let's try with 

my_lower_list = ["a","b","c","d"]
my_upper_list = ["A","B","C","D"]

print("lower case list :",my_lower_list," the upper case list content:",my_upper_list) 

my_lower_list.extend(my_upper_list)

print("Initial lower content:",my_lower_list," the upper list content:",my_upper_list) 

#there are methods also to count the number of words or characters contained in a list

print(my_list_to_count.count(1))

#to find the first index of the first element found

print(my_list_to_count.index('a'))

#another way to add elements on this way to an specific location in the list you can use insert

my_upper_list.insert(0,"0") #add on the begining

print("the upper list content:",my_upper_list) 

my_upper_list.insert(-1,"X") #added in before the last item

print("the upper list content:",my_upper_list) 

#another method used in some practice of stacks is the pop, this simulate taken the last element of the list out

print("pop from the list",my_upper_list.pop())


print("pop from begining the list",my_upper_list.pop(0))

#now we can remove a value specific in the list with remove
my_upper_list.remove('X')

print("removing from the list",my_upper_list)

#in the case that the letter of the element is repeated in the list, remove will do the first one that find 

my_list_to_count.remove('a')


print("removing from the list",my_list_to_count)

# we can play to reverse the content with another method called reverse
my_lower_list.reverse()
print("Initial lower content:",my_lower_list) 

#since reverse it can not be used for strings, we can play with some tricks in the list to reverse the string

my_text = "987654321"

#lest create a list

my_inverted_list = list(my_text) #this split all the content at individual elements

print(my_inverted_list)

#lest do de reverse

my_inverted_list.reverse()


print(my_inverted_list)

#now we can join but with no characters to have the list ready

my_right_text = "".join(my_inverted_list)

print(my_right_text)

#a common method to do is the sort, which will be doing from the lowest to the higher
my_list_to_sort.sort()
print("sorthing this ascendent",my_list_to_sort)

#now lets do the descendent sort this need to be done with a specific argument

my_list_to_sort.sort(reverse=True)
print("sorthing this descendent",my_list_to_sort)

