#as others common languages there is a manage of exepctions that can be happening during the run time 
#lest practice with a list using pop method, if we do continue doing it we will get an empty error

myList = [1,2,3,4]

print(f"pop value {myList.pop()}")
print(f"pop value {myList.pop()}")
print(f"pop value {myList.pop()}")
print(f"pop value {myList.pop()}")

#this kind of error will stop all the code and will kick you out and a way to avoid the general stop is to try block

try:
    print(f"pop value {myList.pop()}")
except:
    print("You can not pop any other data")



#now lets do it more dinamic this to avoid use more lines of code, using the trick with while with not need of iterator as for

mySecondList = [1,2,3,4,5,6,7,7,8,9,7,6,6,6,6]

while(True):
    try:
        print(f"auto pop value {mySecondList.pop()}")
    except:
        print("Automate pop data error, no more data in the list")
        break #this will kill the while


#there is a case when you can use the else in case that there is no error or exception cath means complete well

#lets try a list that ends when a number is 10 pop, if not will reach the end and will fail

myThirdList = [2,3,4,3,4,3,4,3,4,3,4,3] #this list will not have a 10
myForuthList = [3,3,4,3,4,10,4,5,6,7,8,8] #this list have a 10

while(True):
    try:
        val = myThirdList.pop()
        print(f" value pop {val}")
        if val == 10:
            break
    except:
        print("data error, no more data in the list")
        break






#now the execution of the code will end even there is an error in the process
print("EOF")