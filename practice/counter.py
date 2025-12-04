#this will require a simple open file

from io import open
import sys

#we have to create a new file 

file = open('practice/files/counter.txt','a+')
file.seek(0)
content = file.readline()

if len(content) == 0:
    content = '0'
    file.write(content)

file.close()

try:

    counter = int(content)

    if len(sys.argv) == 2:
        if sys.argv[1] == "inc":
            counter += 1
        elif sys.argv[1] == "dec":
            counter -= 1

    print(counter)
           
    file = open('practice/files/counter.txt','w')
    file.write(str(counter))
    file.close()

except:
    print("Error: File is corrupted")
    