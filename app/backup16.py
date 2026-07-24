import sqlite3

conn = sqlite3.connect("dropzone.db")
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, name TEXT, password TEXT)")
conn.commit()

print("===== DropZone =====")
print("1. Register")
print("2. Login")
print("3. Exit")

c = input("Choose: ")

if c == "1":
    name = input("Name: ")
    password = input("Password: ")

    cursor.execute("INSERT INTO users(name,password) VALUES(?,?)", (name,password))
    conn.commit()

    print("Account Created")

elif c == "2":
    name = input("Name: ")
    password = input("Password: ")

    cursor.execute("SELECT * FROM users WHERE name=? AND password=?", (name,password))

    if cursor.fetchone():
        print("Login Successful")
        print("Welcome", name)
    else:
        print("Wrong Login")

else:
    print("Bye")

conn.close()
