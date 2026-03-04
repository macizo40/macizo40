# at this point we just use the methods as is, but what about if we want to send parameters to it

#the idea is that if the methods does get some values in the call, they can be used in the local method for something

def monitoring(funcion):

    def shapping(*args, **kwargs):
        print("\t Before the exec of the method",funcion.__name__)

        funcion(*args, **kwargs)

        print("\t After the execution of the method",funcion.__name__)

    return shapping

@monitoring
def say_hello(name):
    print("Hello again {}".format(name))
@monitoring
def say_godbye(name):
    print(f"Bye bye {name}")

#now let's test the way that we will calling the shapping method
#monitoring(say_hello)()

#now the calling way is not intuitive and what we want is to have a quick way to call the shapping method so before each methond add a @

say_hello("Peter")