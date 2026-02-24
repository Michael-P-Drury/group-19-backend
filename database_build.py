import sqlite3


con = sqlite3.connect("group_19.db")

cursor = con.cursor()

cursor.execute("CREATE TABLE users(username, password)")

con.commit()
