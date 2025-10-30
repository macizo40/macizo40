#modules is a simple way to reuse functions and methods that can be called from other files 

#simple method to print a hello, this only runs when is called
def hello():
    print("Hello from modules.hello()")

#notice that if you have a code or something here in the modules, the code does run when is imported
#lets call the same method

#but the purpose of the modules file is not to have code is more to have methods to reuse, so there is a trick to avoid call the code.

#this class can also have their own constructor
class Hello:
    def __init__(self):
        print("Hello from the modules.constructor()")

#here is where we do introduce this code that will let you import any other file and not run the code

if __name__ == '__main__':
    hello()
