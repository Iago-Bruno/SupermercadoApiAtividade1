import sqlite3

conn = sqlite3.connect("supermarket.sqlite")

cursor = conn.cursor()
sql_query = """ CREATE TABLE categories (
    id integer PRIMARY KEY,
    name text NOT NULL
)"""
cursor.execute(sql_query)