#now that we have create tables and inserting data is moment to move to read them and also modify them.
#we will use the exercise that was done last time with auto incremental and unique values 

import sqlite3

#you need to run the file unique-keys.py first to have the data there in the db
#then you can use the connection to see the data value
myconn = sqlite3.connect("people.db")
mycursor = myconn.cursor()

#now with the cursor will do a select but now using values that we now that exist

mycursor.execute("SELECT * FROM users WHERE clientID=1")

#now with the value get it we need to to fetch it

client = mycursor.fetchone()
#this will be a tuple of the user
print(client)

#now we can update the values that we got as example the name was wrong and we want to update it correctly

mycursor.execute("UPDATE users SET name='Charlote' WHERE clientID=1")

mycursor.execute("SELECT * FROM users WHERE clientID=1")

newname = mycursor.fetchone()
print(newname)

#now we can update more than one value at the same time like 
mycursor.execute("UPDATE users SET age=25,email='charloctocusm@gmail.com' WHERE clientID=1")


#we run again the select and bring the value to be printed
mycursor.execute("SELECT * FROM users WHERE clientID=1")

newname = mycursor.fetchone()
print(newname)

#now finally lets use careful the delete record, always remember WHERE, a simple error in set the condition will delete everything

mycursor.execute("DELETE from users WHERE clientID=1")


myconn.commit()
myconn.close()