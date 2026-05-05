#now lets create the same lambda methods with another one that will help us, is the map

mylist = [2,4,6,8,10,12]

#lets imagine that we want also to apply a method to each element of the list
"""
This simple method will make the number a double of it's own value
"""
def double_number(number):
    return number*2


#now lets use the method map to that function to each elemente of the list

print (list(map(double_number,mylist)))

#the real part is tha a difference from the filter this method does apply action over the elemente, the other is a condition that apply

#lets now do it with the lambda

newlist = map(lambda num: num*2,mylist)

print(list(newlist))

#another common use is when you want to do some changes in list elements, but this need to be the same

one = [2,4,6,8,10]

two = [3,5,7,9,11]

#now lets use a lambda

newvalues = map(lambda a,b: a*b, one,two)

print("the values are: {}".format(list(newvalues)))

#there are no limits regarding the numbers of list these can be also 3 

three = [12,14,16,18,20]

threelist = map(lambda a,b,c: a*b*c, one,two,three)

print("the result of have three list in the lambda is {}".format(list(threelist)))