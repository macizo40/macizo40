#lets now try to add another value with a repeated key from the previous file calles primary-keys.py

import sqlite3

#we do create the connection as usual
myconn = sqlite3.connect("database.db")
mycursor = myconn.cursor()

#remember this is a tuple that was generated the last time in the previous example, but now we need to add the clientID
my_user_list = [
    ('35CHAGM','Chralote',35,'charloctoc@gmail.com'),
    ('40HAOGM','Haomaru',40,'haaahomaruuuu@gmail.com'),
    ('22GALGM','Galford',22,'galfortoc@gmail.com')
]

#now we need to exceute many this record but now will give issues since there are values that can not be repeatable. 

mycursor.executemany("INSERT INTO users VALUES (?,?,?,?)", my_user_list) #check that now we have 4 values so need 4 ?

myconn.commit()
myconn.close()



