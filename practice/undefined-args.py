#lets start the method when the arguments are not defined, this is known as undefined arguments

def undefined_args(*args):
    print(args)

#lets test this method to see which are the values that will be printed

undefined_args(5,"hello",[1,2,3,4,5])

#the whole list of the values is a tuple which is inmutable, it means can not be changed any of their values

#something that we can do is that the values need to be iterable

def iterator_undefined(*args):
    for arg in args:
        print(arg)


iterator_undefined(1,"bye",[6,7,8,9])

#another very good approach of use this unidefined values are to create a dictionary and the way to create it is the next using two *

def undefined_keynames(**kwargs):
    print(kwargs)


#lets pass this new values but now with a key=value format

undefined_keynames(n=4,t="text",l=[1,2,3,4])

#now lets iterate the dictionary with the dale rule but now using the key and value

def iterate_keynames(**kwargs):
    for kwarg in kwargs:
        print(kwarg,"=",kwargs[kwarg])

#now lets pass the new values

iterate_keynames(n=6,t="new text",l=[5,6,7,8])


#now the key usage of this is to combine a super function that can get undefined values and use them in both ways


def super_undefined(*args,**kwargs):
    #example using all the args like numnbers to do a math operation
    total=0
    for arg in args:
        total += arg
    print("total values are in ",total)

    #now let use all the key value arguments

    for kwarg in kwargs:
        print(kwarg,"=",kwargs[kwarg])


#now lets pass as many possible values with simple args or key value

super_undefined(1,2,3,4,5,6,7,n=6,t="super text",list=['a','b','c'])


