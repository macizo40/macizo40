#lets back a little with the list and the way that those are handling elements

#basic method to add elements to the list

mylist = [] #empty list
for value in 'letters': # we will go for each letter in the string lenght and save it in the value 
    mylist.append(value)

print(f"here is the list now {mylist}")

#now lets see a more advanced method

mysecondlist = [letter for letter in 'letters']#you can see that refering to the same value where is stored by the for, it's gets append

print(f"take a look to the second list {mysecondlist}")

#lets now see a traditional method ofr maths process

number_list = []
for number in range(0,11):#this will run the values for 10 times
    number_list.append(number**2)

print(number_list)

#now with the advanced method we will have 

second_number_list = [number**2 for number in range(0,11)]

print(second_number_list)

#lets now see how we can mmanage some conditions inside the list creation, lets see this traditional method

third_list = []
for number in range(0,11):
    if number % 2 == 0:
        third_list.append(number)

print("third list is {}".format(third_list))

# now lets create with a third mode of the method:

condition_in_list = [number for number in range(0,11) if number % 2 == 0]

print(condition_in_list)