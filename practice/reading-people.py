#importing the cvs since we need to use a delimiter to transform the file
import csv

#lets create a variable where we will be saving objects from the reader

people_list = []

fields = ['identifier','name','last_name','nationality','gender'] #this will be the headers in the file


#now is time to load the file, using the values of previous method except that we do not need to specify the read attribute
with open('practice/files/mypeoplelist.txt', newline='\n') as cvsfile: #no need special attribute specification
    #intead of a writer now we need a reader
    reader = csv.reader(cvsfile,delimiter=';') #reading the file
    #but also the benefit is that we can get back from reader eac h attribute alone
    for identifier, name, last_name, nationality, gender in reader:
        print(identifier,name)
        people_list.append({'identifier':identifier,'name':name,'last_name':last_name,'nationality':nationality,'gender':gender})

print(people_list)

#this requieres a little more of details but the result is great
with open('practice/files/mypeoplelist.csv','w',newline='\n') as cvsfile:   
    writer = csv.DictWriter(cvsfile,fieldnames=fields) #you can see that parameters are fields too
    writer.writeheader() #this method is escencial to first write the headers
    #time to write but this time different since we are using a dictionary
    for people in people_list:
        writer.writerow (people)
