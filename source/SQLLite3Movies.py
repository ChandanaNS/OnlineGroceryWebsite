
import sqlite3


conn = sqlite3.connect('moviestrial.db')
print("Opened database successfully")
#
#Creating a table
# conn.execute('''CREATE TABLE moviestrial
#          (ID INT PRIMARY KEY     NOT NULL,
#          NAME           TEXT    NOT NULL,
#          DURATION            INT     NOT NULL,
#          DATE        CHAR(50));''')
#
# print("Table created successfully")

#inseting values
# conn.execute("INSERT INTO moviestrial (ID,NAME,DURATION,DATE) \
#       VALUES (1, 'kjd', 160, '21/1/2020')");
#
# conn.execute("INSERT INTO moviestrial (ID,NAME,DURATION,DATE) \
#      VALUES (2, 'kjd', 160, '21/1/2020')");
# conn.execute("INSERT INTO moviestrial (ID,NAME,DURATION,DATE) \
#     VALUES (3, 'kjd', 160, '21/1/2020')");
# conn.execute("INSERT INTO moviestrial (ID,NAME,DURATION,DATE) \
#      VALUES (4, 'kjd', 160, '21/1/2020')");


#fetching table
cursor = conn.execute("SELECT ID,NAME,DURATION,DATE from moviestrial")
for row in cursor:
   print("ID = ", row[0])
   print("NAME = ", row[1])
   print("DURATION = ", row[2])
   print("DATE = ", row[3], "\n")

conn.commit()
print("Records created successfully")
conn.close()