#lets now try to work with input this is a great example to make sure the content that you introduce it is fine

while (True):
    try:
        number = float(input("Type a number: "))
        n =4
        print("{}/{}={}".format(number,n,number/n))
    except:
        print("something wrong just happen, try again with a number")
    else:
        print("all looks good")
        break
    finally:
        print("End of Line")