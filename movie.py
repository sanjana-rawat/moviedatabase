import sqlite3

try:
    sqliteConnection = sqlite3.connect('SQLite_Python.db')
    cursor = sqliteConnection.cursor()
    print("Database created and Successfully Connected to SQLite")

    sqlite_select_Query = "select sqlite_version();"
    cursor.execute(sqlite_select_Query)
    record = cursor.fetchall()
    print("SQLite Database Version is: ", record)

    sql =''' CREATE TABLE IF NOT EXISTS MOVIES4(
            MOVIE_NAME CHAR(50) NOT NULL,
            ACTOR_NAME CHAR(25),
            ACTRESS VARCHAR(25),
            RELEASE_YEAR NUMBER(4),
            DIRECTOR_NAME VARCHAR(25)  )'''
    cursor.execute(sql)
    print("Table created successfully........")

    cursor.execute('''INSERT INTO MOVIES4 VALUES ('URI', 'VICKY KAUSHAL', 'YAMI', 2019,'ADITYA')''')
    cursor.execute('''INSERT INTO MOVIES4 VALUES ('KASHMIR FILES','DARSHAN','pallavi',2022,'vivek')''')
    cursor.execute('''INSERT INTO MOVIES4 VALUES ('3 IDIOTS', 'AAMIR HAN','KAREENA',2009, 'RAJKUMAR')''')
   
    def actorfetch(actor):
        data=cursor.execute("SELECT * FROM MOVIES4 WHERE ACTOR_NAME=?",(actor,))
        for row in data:
           print(row)

    # Display data inserted
    print("Data Inserted in the table: ")
    data=cursor.execute('''SELECT * FROM MOVIES4''')
    for row in data:
      print(row)
    print("\n\n")
    actorfetch('VICKY KAUSHAL')
    cursor.close()


except sqlite3.Error as error:
    print("Error while connecting to sqlite", error)
finally:
    if sqliteConnection:
        sqliteConnection.close()
        print("The SQLite connection is closed")
