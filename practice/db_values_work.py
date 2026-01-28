#after the data base is created and it contains a value, now lets move to start getting the values from the DB
#we will use a new file to work to avoid be creation steps
import sqlite3

conn = sqlite3.connect("database.db")

mycursor = conn.cursor()

table_name = "users"
#we will not use many variables now but lets recover the values first

mycursor.execute("SELECT * FROM {}".format(table_name))

#at this point now mycursor does have the value sin a json format, but we cannot just print them, we need to fetch them with a new object
result = mycursor.fetchone() #as you can see here we just recover one value, the format of the value is a tuple
print(result) #you can confirm with this that is tuple and you can access to values with their position []

#now we can handle the result with a tuple by positions and play with them as this
print(f"Hello my name is {result[0]}, my age is {result[1]} and my email is {result[2]}") 

#as we did with the files we need to close the connection
conn.close()