import sqlite3

#we need a conection to the current db
conn = sqlite3.connect("database.db")

#the cursor is important always

mycursor = conn.cursor()

#this is the name of the table inside the db where we will add information
table_name = "users"

#this will return a lot of values, all of them in form of a tuple
mycursor.execute("SELECT * FROM users")

#the object mycursor now has the returned values of the query we need then to assign them to a list
table_users = mycursor.fetchall() #this method brings alll the values not just one

#this is a list and we can just print it now 
print(table_users)

#now we can read one by one and do all the work that we want

for user in table_users:
    print("this is the user tuple {}".format(user))

#we need to commit
conn.commit()
conn.close()
