#lets now start working with files called comma seperated values which are the common to store data in sheets

#we need to import csv
import csv

#you have a list of tuples, that are different colums, each tuble has identifier, name, phone number with code area and age
clients = [
    (1,'Peter','1121324351','25'),
    (2,'John','1133334455','27'),
    (3,'Sara','2111346645','45')
    ]

#this time we will use a different method to open files the method with, this method does not need a close action in files.
with open('practice/files/my_clients_file.cvs','w',newline='\n') as cvsfile: #newline is the character that will assign to each row
    #new concetp is to have a writer, which will be the one handling the file
    writer = csv.writer(cvsfile,delimiter=',') #as you can see here the delimiter is each coma will be separating values
    #time to store the data for each element in the list of tuples
    for client in clients:
        writer.writerow(client) 


#now is time to load the file, using the values of previous method except that we do not need to specify the read attribute
with open('practice/files/my_clients_file.cvs', newline='\n') as cvsfile: #no need special attribute specification
    #intead of a wirter now we need a reader
    reader = csv.reader(cvsfile,delimiter=',') #reading the file
    #but also the benefit is that we can get back from reader eac h attribute alone
    for identifier, name, phone_number, age in reader:
        print(identifier,name)


#something more advance and with more format insted of use list lets use a dictionary

#you have a list of tuples, that are different colums, each tuble has identifier, name, phone number with code area and age
companies = [
    (1,'IBM','567586','100000'),
    (2,'Google','46574','20000'),
    (3,'HP','35465','40000')
    ]

#this requieres a little more of details but the result is great
with open('practice/files/my_company_file.cvs','w',newline='\n') as cvsfile:
    fields = ['identifier','name','code','employees_number'] #this will be the headers in the file
    writer = csv.DictWriter(cvsfile,fieldnames=fields) #you can see that parameters are fields too
    writer.writeheader() #this method is escencial to first write the headers
    #time to write but this time different since we are using a dictionary
    for identifier, name, code, employees_number in companies:
        writer.writerow({
            "identifier":identifier, "name":name,"code":code,"employees_number":employees_number
        })

#the reader follows the same logic but this will be with a different reader and the content need to read as a dictionary, key:value
#now is time to load the file, using the values of previous method except that we do not need to specify the read attribute
with open('practice/files/my_company_file.cvs', newline='\n') as cvsfile: #no need special attribute specification
    #intead of a wirter now we need a reader
    reader = csv.DictReader(cvsfile) #we do not need a delimiter this time is automatic
    #but also the benefit is that we can get back from reader eac h attribute alone
    for company in reader: #we need to use an object that will contains the key:value
        print(company["identifier"],company["name"],company["code"],company["employees_number"])#we will print using keys
