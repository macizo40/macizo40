

value=10

def returning_value(value):
    value=value+10
    print("Values inside the function is: {}".format(value))
    return value

value=returning_value(value)
print("Values outside the function is: {}".format(value))


#now there will be a multiple asignation with the order that I want

def several_types():
    text = "Here is a text"
    number = 50
    myList = [1,2,3]

    return text,number,myList

outText,outNumber,outList=several_types()

print("Values that are now out, text {}, number {}, list {}".format(outText,outNumber,outList))

def par_o_impar(numero):
    if numero % 2 == 0:
        print("PAR")
    else:
        print("IMPAR")

par_o_impar(outNumber)

