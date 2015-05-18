#!/usr/bin/env python

#Create a SQLite3 databse and table

#import the sqlite3 library
import sqlite3

#create new database if the databse dosen't exist already
conn = sqlite3.connect("cars.db")

#get a cursor object used to execute SQL commands
cursor = conn.cursor()

#create a table
cursor.execute("""CREATE TABLE inventory
(Make TEXT, Model TEXT, Quantity INT)
""")

#close the database connection
conn.close()