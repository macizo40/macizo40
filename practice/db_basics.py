#it is time to start the work with Data Bases, we will be using SQLite a powerful free DB

import sqlite3

#we need to create an object to stablish the connection and creation(if does not exist) to the DB
conn = sqlite3.connect("database.db")

#to execute any SQL statement they are run as huge string, my recomendation and thanks to python, you can split it
#lets create a combination of values to run the create table query

table_name = "users"
sql_statement = "CREATE TABLE"
sql_colums = "name VARCHAR(100), age INTEGER, email VARCHAR(100)"

#it is better to combine it all ina single string
sql_string = sql_statement + " " + table_name + " " + "(" + sql_colums + ")"

#lets see how the entire statement does looks like first:

print(sql_string)

#to start doing sql statements we need an object that we will call it cursor, this is inside the connection object created
mycursor = conn.cursor()

#now with the cursor create we do execute the statement
mycursor.execute("{} {} ({})".format(sql_statement,table_name,sql_colums))#this is an string so is better to user format 

#now that the table is created we can start to add more values to it, let's create also some strings to play with previous variables

sql_statement="INSERT INTO"
#lets use an string to play with diferrent values, remember that strings inside strings need to use the '', since the values are varchar
sql_value1 = "'Ukyo',25,'tachibana@gmail.com'"

#we need to execute again the cursors statement
mycursor.execute("{} {} VALUES({})".format(sql_statement,table_name,sql_value1))

# to confirm the insertion we need to do a commit
conn.commit()
#as we did with the files we need to close the connection
conn.close()