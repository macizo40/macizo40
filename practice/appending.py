from io import open

#we will use a different method to prove that append also creates the file from scratch 
myfile = open('practice/files/mypointer.txt','a')

myfile.write("This is the first line and from here we will have lines with numbers\n")

for i in range(50):
    mytext = f'{i}\n'
    if i != 0:
        myfile.write(mytext)


myfile.close()