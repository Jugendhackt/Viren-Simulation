import sqlite3

conn = sqlite3.connect("books.sqlite")

cursor = conn.cursor()
#sql_query = """ CREATE TABLE book (
    #id integer PRIMARY KEY AUTOINCREMENT,
    #author text NOT NULL,
    #language text NOT NULL,
    #title text NOT NULL
#)"""

sql_query = "create table users(id INTEGER PRIMARY KEY AUTOINCREMENT,results int(15));"
cursor.execute(sql_query)