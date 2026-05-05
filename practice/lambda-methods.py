#now lets take a look to the lambda functions and how are they construct, but first we need to descontruc it to show the functionality

#lest start with a simple method to understand more
"""
This method will let us multiply the number by 2
"""
def multiply(number):
    result = number * 2
    return result

#now a simple calling of the method

print("number is {}".format(multiply(3)))

#a way to just simplify it to its minimun level is 

def plus(number): return number*2

print("a single method line is {}".format(plus(2)))

#now lets see how it changes using a lambda function with the same logic a number multiply by 2, but this need to assigned to a variable

mylambda = lambda num: num * 2

#now we call it as usual like other methods calls

print(f"my result from a lambda is {mylambda(4)}")

#lets recall when we have to identify if a number is par or not, we have to set a whole method, but now with lambda we can do it

isnot_par = lambda num: num%2 != 0

print("lets test this is not par of 4 is {}".format(isnot_par(4)))

#lets use with strings as example we do have a simpre lambda method that will revert any string with slicing quick method that we used

revert = lambda mystring: mystring[::-1]

#now we can revert any string no mather which one

print("lets rever 'tachibana' is now {}".format(revert('tachibana')))

#we can use more than a single value, but the calls need to be done with commas too 

multiplier = lambda a,b : a*b

#check now how is called with two simple values as objects

print("now use the method with two value calling {}".format(multiplier(2,4)))
