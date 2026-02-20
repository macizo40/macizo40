#now in this practice lets start using unique values, as we did like with users, we can have unique and autoincremental values

#we will use the same exercise as before:

# on this practice we will be taking some practices with the primary keys in the data base
import sqlite3

myconn = sqlite3.connect("people.db")
mycursor = myconn.cursor()

#the primary key now is an integer and autoincrement since will be a value that automatically increment
mycursor.execute('''
    CREATE TABLE users (
                 clientID INTEGER PRIMARY KEY AUTOINCREMENT,
                 taxid VARCHAR(13) UNIQUE,
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

mycursor.executemany("INSERT INTO users VALUES (null,?,?,?,?)", my_user_list) #check that now we have 5 values so need 4 ? and one null

myconn.commit()
myconn.close()
