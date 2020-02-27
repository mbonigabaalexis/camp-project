# import mysql.connector

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   passwd="",
#   database="cobanga"
# )

# mycursor = mydb.cursor()

# sql = "INSERT INTO student (name, address) VALUES (%s, %s)"
# val = [
#   ('madina', 'mugera'),
#   ('alexis', 'nyabiheke'),
#   ('gaetan', 'nyarubuye'),
#   ('muhoza', 'mugera'),
#   ('bonke', 'kigali'),
#   ('ben', 'kabarore')
  
# ]

# mycursor.executemany(sql, val)

# mydb.commit()

# print(mycursor.rowcount, "was inserted.")


import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="cobanga"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM student ORDER BY name")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)


#select any colum

#fetch 

# import mysql.connector

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   passwd="",
#   database="cobanga"
# )

# mycursor = mydb.cursor()

# mycursor.execute("SELECT name, address FROM student")

# myresult = mycursor.fetchall()

# for x in myresult:
#   print(x)

#delete
# import mysql.connector

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   passwd="",
#   database="cobanga"
# )

# mycursor = mydb.cursor()

# sql = "DELETE  FROM student WHERE address ='kigali'"

# mycursor.execute(sql)

# mydb .commit()

# print(mycursor.rowcount,"record(s) deletect")
#update
# import mysql.connector

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   passwd="",
#   database="cobanga"
# )

# mycursor = mydb.cursor()
# sql="UPDATE student SET address='NGARAMA' WHERE address='mugera'"

# mycursor.execute(sql)
# mydb.commit()
# print(mycursor.rowcount,"RECORD(s) efffected")