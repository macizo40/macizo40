import sqlite3

#we need a conection to the current db
conn = sqlite3.connect("database.db")

#the cursor is important always

mycursor = conn.cursor()

#this is the name of the table inside the db where we will add information
table_name = "users"

#lets create a list to handle the several users just like the first one
#remember this is a tuple
my_user_list = [
    ('Chralote',35,'charloctoc@gmail.com'),
    ('Haomaru',40,'haaahomaruuuu@gmail.com'),
    ('Galford',22,'galfortoc@gmail.com')
]

#now that we have the list lets use the cursor to insert them, check the way to insert with the ? symbol

mycursor.executemany("INSERT INTO users VALUES (?,?,?)", my_user_list)

#we need to commit
conn.commit()
conn.close()