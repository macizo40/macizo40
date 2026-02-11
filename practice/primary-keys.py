# on this practice we will be taking some practices with the primary keys in the data base
import sqlite3

myconn = sqlite3.connect("database.db")
mycursor = myconn.cursor()

#the primary keys are values that are not repeatable and unique in this case can be like employee or client ids
mycursor.execute('''
    CREATE TABLE users (
                 clientID VARCHAR(10) PRIMARY KEY,
                 name VARCHAR(100), 
                 age INTEGER, 
                 email VARCHAR(100)
        )
''') #check this trick of using tree simple ' to let you write the query

#remember this is a tuple but now we need to add the clientID
my_user_list = [
    ('35CHAGM','Chralote',35,'charloctoc@gmail.com'),
    ('40HAOGM','Haomaru',40,'haaahomaruuuu@gmail.com'),
    ('22GALGM','Galford',22,'galfortoc@gmail.com')
]

#now we need to exceute many this record

mycursor.executemany("INSERT INTO users VALUES (?,?,?,?)", my_user_list) #check that now we have 4 values so need 4 ?

myconn.commit()
myconn.close()
