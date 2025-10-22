#now lets see the most commons methods to handle lists

my_initial_list = [1,2,3,4,5,6]
my_list_to_count = [1,1,1,1,1,'hola','hola','a','a','a']

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