#!/usr/bin/python2.7

import sqlite3

conn=sqlite3.connect('user.db')

cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
	id INTERGER
	name TEXT
)
""")
conn.commit()
