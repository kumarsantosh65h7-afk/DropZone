
import sqlite3

conn = sqlite3.connect("dropzone.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY,
    name TEXT,
    password TEXT
)
""")

conn.commit()

print("===== DropZone =====")
print("1. Register")
print("2. Login")
print("3. Exit")

choice = input("Option choose karo: ")

if choice == "1":
    name = input("Name: ")
    password = input("Password: ")

    cursor.execute(
        "INSERT INTO users(name,password) VALUES(?,?)",
        (name,password)
    )

    conn.commit()
    print("Account create ho gaya")

elif choice == "2":
    name = input("Name: ")
    password = input("Password: ")

    cursor.execute(
        "SELECT * FROM users WHERE name=? AND password=?",
        (name,password)
    )

    user = cursor.fetchone()

    if user:
        print("Login Successful")
        print("Welcome", name)
    else:
        print("Wrong Login")

elif choice == "3":
    print("Bye")

else:
    print("Wrong option")

conn.close()
