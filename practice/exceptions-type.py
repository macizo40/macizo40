#in this we will learn how to catch different types of exception to show the specific action of each one

while (True):
    try:
        number = float(input("Type a number: "))
        n =4
        print("{}/{}={}".format(number,n,n/number))
    except TypeError: #here we are just saying that if type is wrong we catch it
        print("something wrong just happen, try again with a number")
    except ValueError:
        print("could not convert string to float")
    except Exception as e:
        print(type(e).__name__) #this trick will teel you the name of any expection caught in run time
    else:
        print("all looks good")
        break
    finally:
        print("End of Line")