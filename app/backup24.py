import sqlite3

conn = sqlite3.connect("dropzone.db")
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS users(username TEXT,password TEXT,uid TEXT,game TEXT,region TEXT)")
conn.commit()

while True:
    print("\n===== DropZone =====")
    print("1. Register")
    print("2. Login")
    print("3. Exit")

    ch = input("Choose: ")

    if ch == "1":
        u = input("Username: ")
        p = input("Password: ")
        uid = input("Free Fire UID: ")
        game = input("Game Name: ")
        reg = input("Region: ")

        cursor.execute(
            "INSERT INTO users VALUES(?,?,?,?,?)",
            (u,p,uid,game,reg)
        )
        conn.commit()

        print("Account Created")

    elif ch == "2":
        u = input("Username: ")
        p = input("Password: ")

        cursor.execute(
            "SELECT * FROM users WHERE username=? AND password=?",
            (u,p)
        )

        data = cursor.fetchone()

        if data:
            print("Login Successful")
            print("Username:",data[0])
            print("Free Fire UID:",data[2])
            print("Game Name:",data[3])
            print("Region:",data[4])
        else:
            print("Wrong Login")

    elif ch == "3":
        break

    else:
        print("Wrong Option")

conn.close()
