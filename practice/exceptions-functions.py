#lets start to see how the thing are handle in functions and how to call them manually

def readValue (value=None):
    try:
        if value is None:
            raise ValueError("This is a value error") #this is the method to call the exception
    except ValueError:
        print("Out of the call expection")

readValue()