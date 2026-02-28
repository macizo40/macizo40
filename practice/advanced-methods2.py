#lets continue working in some methods that will help to understend more the glbals and locals environments


#with the two methods that were there before now we want to monitor the execution of those

def monitoring(funcion):

    def shapping():
        print("\t Before the exec of the method",funcion.__name__)

        funcion()

        print("\t After the execution of the method",funcion.__name__)

    return shapping

@monitoring
def say_hello():
    print("Hello again")
@monitoring
def say_godbye():
    print("Bye bye")

#now let's test the way that we will calling the shapping method
monitoring(say_hello)()

#now the calling way is not intuitive and what we want is to have a quick way to call the shapping method so before each methond add a @

say_hello()