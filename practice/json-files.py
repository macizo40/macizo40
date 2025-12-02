#there is another very common used files to handle information those are the json files, which are key:value type

#we start importing json

import json

#if we use the same types of list:

clients = [
    (1,'Peter','1121324351','25'),
    (2,'John','1133334455','27'),
    (3,'Sara','2111346645','45')
    ]

#this is the advanced part of json, in a dictionary you can use a key to identify types of that, and in values, is a whole
#listof common data, as example in the next dictionary we will sale as clients all the data from the list as this:

data = {"clients":[]} #clients is the key to find the list of clients, inside the list will be items to load of each client

#lets dinamically fill the data list

for id, name, phone_number, age in clients:
    #we need to tell that dats in the key clients will have a list of individual data of each client
    data['clients'].append({"id":id,"name":name,"phone_number":phone_number,"age":age}) 
#let's print data and see the info:
print("Here is the data \n",data)

#now with is going to be our more common method to write the data in the files:
with open('practice/files/my_clients_file.json','w') as jsonfile:
    #we will not use a writer this time we send it like json methid
    json.dump(data,jsonfile)

#lets clean the data list now to bring the information back from the file
data = None

print("Confirming that data is now clean:",data,"\n")

#to open the file again is just with and the name of the file
with open('practice/files/my_clients_file.json') as jsonfile:
    #now we will be adding all the info from the file to the list data
    data = json.load(jsonfile)
    #since for an specific set of data there is a key, we need to load it by the key general of the data type
    for client in data['clients']: 
        #now client is a list but is a list of dictionaries, so this should be the way to acces to each row
        print(client["id"],client["name"],client["phone_number"],client["age"])

