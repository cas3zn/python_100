import sqlite3

# creating a connection to a new database
db = sqlite3.connect("books-collection.db") 

# creating a cursor that will control our database
cursor = db.cursor()

# create the table
cursor.execute("CREATE TABLE textbooks (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL )")

# Insert values into the table
cursor.execute("INSERT INTO textbooks VALUES(1,'Harry Potter','J.K. Rowling','9.3')")

# commit changes to the db
db.commit()