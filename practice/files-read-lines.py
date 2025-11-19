from io import open


myfile = open('practice/files/myfile.txt','r')

#on this example the lines each of them willbe stored in a list type, using the method readlines

myLines = myfile.readlines()

for i in myLines:
    print("content of the files is ",i)

#this method finalize the use and the write

myfile.close()

#lets now try to open the file with append mode, this will add the content at the EOF 

myfile = open('practice/files/myfile.txt','a')

myfile.write('\nAdding a last line at the EOF')

myfile.close()





