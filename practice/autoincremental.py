#in the case that we want that some values does not gets repeated and there are not need to set the primary keys
#we can work with autoincremental values for making sure the values will not repeat

import sqlite3

#we do create the connection as usual with a new DB
myconn = sqlite3.connect("products.db")
mycursor = myconn.cursor()

#lets first create a table to insert products

#the primary keys are values that are not repeatable and unique in this case can be like employee or client ids
mycursor.execute('''
    CREATE TABLE products (
                 productID INTEGER PRIMARY KEY AUTOINCREMENT,
                 productName VARCHAR(100) NOT NULL, 
                 brand VARCHAR(100) NOT NULL, 
                 price FLOAT NOT NULL
        )
''') #check this trick of using tree simple ' to let you write the query

#now lets insert the values and lets see how insert an autoincremental value in the table

#remember this is a tuple and we will just manange 3 values that are different
my_user_list = [
    ('perfum','poison girl',3500.00),
    ('tv','Hiansense',4000.00),
    ('speaker','bosse',2223.00)
]

#now we need to exceute many this record but now will give issues since there are values that can not be repeatable. 

mycursor.executemany("INSERT INTO products VALUES (null,?,?,?)", my_user_list) 
#check that now we have 3 custom values so need ? but autoincremental need null


# we do close the connection and commit the changes
myconn.commit()
myconn.close()
