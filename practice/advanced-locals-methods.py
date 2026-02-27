#lets again review the processing of the local environments, those are interns and visible only inside methods

i_am_global_number = 46

def say_hello():
    #this variables and methods are onyl visible inside the main method, they do not exist in the global environment 
    my_number= 45
    def hi_messge():
        return "Hello I am local" 

    print(locals())

    return hi_messge

print(say_hello())

#to view all the global environment object we can use this method

print(globals())

#it is interesting that locals and globals are in short term values in a huge dictionary and they are values that you can use

print("here is the number from the globals:",globals()['i_am_global_number'])

#but in the past we still not execute the method this a way which is kind of strange but it works

print("this is the method inside the method result",say_hello()())

#other way is to assign the return to a variable like this

storing_method_result = say_hello()

#after this the variable becomes a method and the way to get the values is to call it as method with ()

print("I am coming from a method inside antoher method:",storing_method_result())

#now lets review some new concept to send a method as an argument to another method

def method_as_argument():
    return "I am a argument"

def method_calling_methods(funcion):
    print(funcion())

#not lets test sending the method as argument

method_calling_methods(method_as_argument)