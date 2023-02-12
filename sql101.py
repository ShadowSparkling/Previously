#BASIC SCRIPT FOR CONNECTING TO THE DATABASE OF MYSQL & creating a database.

# import mysqli.connector
# mydb = mysqli.connector.connect(
#     host = "localhost",
#     username = "yourusername",
#     password = "yourpassword"
# )
# mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE mydatabase")



#CREATING A TABLE "customers" in DATABASE "mydatabase".

# import mysqli.connector
# mydb = mysqli.connector.connect(
#     host = "localhost",
#     username = "yourusername",
#     password = "yourpassword",
#     database = "mydatabase"
# )
# mycursor = mydb.cursor()

# mycursor.execute("CREATE TABLE customers 
# (id INT AUTO-INCREMENT PRIMARY KEY,
#  name VARCHAR (255),
#  address VARCHAR (255)"
# )



#INSERTING A RECORD in the database.

# import mysqli.connector
# mydb = mysqli.connector.connect(
#     host = "localhost",
#     username = "yourusername",
#     password = "yourpassword",
#     database = "mydatabase"
# )

# mycursor = mydb.cursor()

# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = ("John", "Highway 21") #If there are more than one value to insert then write like this: val = [("x","y"),("a","b")]

# mycursor.execute(sql, val) #If there are more than one value to insert use mycursor.executemany()
# mydb.commit()

# print(mycursor.rowcount," record inserted.")
# print("The ID of the last row insertion is", mycursor.lastrowid)


#To SSELECT AND SHOW all the records in the database.

# import mysqli.connector
# mydb = mysqli.connector.connect(
#     host = "localhost",
#     username = "yourusername",
#     password = "yourpassword",
#     database = "mydatabase"
# )

# mycursor = mydb.cursor()

# mycursor.execute("SELECT * FROM customers") #same as mycursor.execute("SELECT name, address FROM customers")
# myresult = mycursor.fetchall()  #The method fetchone() returns only the first row of the records.

# for x in myresult:
#     print(x)


# Use of WHERE 

# import mysqli.connector
# mydb = mysqli.connector.connect(
#     host = "localhost",
#     username = "yourusername",
#     password = "yourpassword",
#     database = "mydatabase"
# )

# mycursor = mydb.cursor()

# sql = "SELECT * FROM customers WHERE address = 'Park Street'" #'%way%' this is a wildcard that means that it will choose anything with the word way in it.

# mycursor.execute(sql)

# myresult = mycursor.fetchall()

# for x in myresult:
#     print(x)


#Ordering the columns by ORDER DESC in descending order.

# import mysqli.connector
# mydb = mysqli.connector.connect(
#     host = "localhost",
#     username = "yourusername",
#     password = "yourpassword",
#     database = "mydatabase"
# )

# mycursor = mydb.cursor()

# sql = "SELECT * FROM customers ORDER BY name" #For descending order use ORDER BY name DESC

# mycursor.execute(sql)
# myresult = mycursor.fetchall()
# for x in myresult:
#     print(x)



#DELETING a RECORD.

# import mysqli.connector
# mydb = mysqli.connector.connect(
#     host = "localhost",
#     username = "yourusername",
#     password = "yourpassword",
#     database = "mydatabase"
# )

# mycursor = mydb.cursor()

# sql = "DELETE FROM customers WHERE address = 'Unknown'"
# mycursor.execute(sql)
# mydb.commit()

# print(mycursor.rowcount," record(s) deleted")

# #OR

# sql = "DELETE FROM customers WHERE address = %s"
# adr = ("Unknown",)

# mycursor.execute(sql, adr)
# mydb.commit()

# print(mycursor.rowcount," record(s) deleted")




#DELETING A TABLE

# import mysqli.connector
# mydb = mysqli.connector.connect(
#     host = "localhost",
#     username = "yourusername",
#     password = "yourpassword",
#     database = "mydatabase"
# )

# mycursor = mydb.cursor()

# sql = "DROP TABLE customers" #For descending order use ORDER BY name DESC

# mycursor.execute(sql)



#UPDATING a record

# import mysqli.connector
# mydb = mysqli.connector.connect(
#     host = "localhost",
#     username = "yourusername",
#     password = "yourpassword",
#     database = "mydatabase"
# )

# mycursor = mydb.cursor()

# sql = "UPDATE customers SET address = %s WHERE address = %s"
# adr = ("Another Realm beyond humanity", "unknown")

# mycursor.execute(sql, adr)
# mydb.commit()  #THIS IS CRUCIAL, IF NOT WRITTEN IT WON'T DO THE COMMAND.
# print(mycursor.rowcount,"row(s) affected.")



#PUTTING A LIMIT TO SHOWING RESULTS.

# import mysqli.connector
# mydb = mysqli.connector.connect(
#     host = "localhost",
#     username = "yourusername",
#     password = "yourpassword",
#     database = "mydatabase"
# )

# mycursor = mydb.cursor()

# sql = "SELECT * FROM customers LIMIT 5 OFFSET 2"

# mycursor.execute(sql)

# myresult = mycursor.fetchall()

# for x in myresult:
#     print(x)



#JOINING TWO TABLES

import mysqli.connector
mydb = mysqli.connector.connect(
    host = "localhost",
    username = "yourusername",
    password = "yourpassword",
    database = "mydatabase"
)

mycursor = mydb.cursor()

sql = "SELECT \
    users.name AS user, \
    products.name AS favorite \
    FROM users \
    INNER JOIN products ON user.fav = products.id"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)










