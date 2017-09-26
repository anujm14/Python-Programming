#Import SQL Lite database
import sqlite3
#Create a database connection
conn = sqlite3.connect('DSS.db')
#Define cursor
c = conn.cursor()

#Create table
def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS dssCourses(code INTEGER, startDate TEXT, day TEXT, name TEXT)')

#Insert Data into Table
def data_entry():
    c.execute("INSERT INTO dssCourses VALUES(615, '2017-08-29', 'Tuesday', 'Python Programming')")
    conn.commit()
    c.close()
    conn.close()

create_table()
data_entry()
