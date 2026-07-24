import sqlite3

conn = sqlite3.connect("dropzone.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS players(
id INTEGER PRIMARY KEY,
name TEXT,
match_name TEXT
)
""")

conn.commit()

name = input("Player Name: ")

match = input("Match Name: ")

cursor.execute(
"INSERT INTO players(name,match_name) VALUES(?,?)",
(name,match)
)

conn.commit()

print("Match Join Successful")

print("\n===== Joined Players =====")

cursor.execute("SELECT * FROM players")

for p in cursor.fetchall():
    print(p[1], "-", p[2])

conn.close()
