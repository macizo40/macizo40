#now lets explode more the lambda area that will be using with the filter method to give more power

#lets again try to decompose how the lambda will interact with the filter

#write a simple method that finds multiple of 3

#we have a list 

mylist = [1,3,4,2,5,78,65,45,32]

#an usual method to work is the next

def multiple(number):
    if number % 3 == 0:
        return True

#now let use the method filter, you can see that we will send the method and the list as arguments

print("this is the return of the filter method:",filter (multiple,mylist))

#the previous output is just an object so you need to save it to be iterable in an new object

filter_list = filter (multiple,mylist)
#we need to cast it, or transform it to see the result 
print("now lets see how it does ",list(filter_list))

#as the filter list is an iterable object you can use the next to see the value without cast it, 
# this need to be a new object since references will throw an error
f = filter (multiple,mylist)
print("using the next you get:",next(f))

print("using the next you get:",next(f))

#now lets use a lambda to avoid have a whole method

second_list = filter(lambda n:n%3==0,mylist)

print("from the new list the next you get:",next(second_list))

print("frim the new list the next you get:",next(second_list))
