import sqlite3

conn = sqlite3.connect("dropzone.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
username TEXT,
password TEXT,
uid TEXT,
game TEXT,
region TEXT
)
""")

conn.commit()

while True:

    print("\n===== DropZone =====")
    print("1. Register")
    print("2. Login")
    print("3. Exit")

    ch = input("Choose: ")

    if ch == "1":

        username = input("Username: ")
        password = input("Password: ")
        uid = input("Free Fire UID: ")
        game = input("Game Name: ")
        region = input("Region: ")

        cursor.execute(
            "INSERT INTO users VALUES(?,?,?,?,?)",
            (username, password, uid, game, region)
        )

        conn.commit()
        print("Account Created")

    elif ch == "2":

        username = input("Username: ")
        password = input("Password: ")

        cursor.execute(
            "SELECT * FROM users WHERE username=? AND password=?",
            (username, password)
        )

        user = cursor.fetchone()

        if user:
            print("\nLogin Successful")
            print("Welcome", user[0])

            while True:

                print("\n===== Dashboard =====")
                print("1. View Profile")
                print("2. Logout")

                option = input("Choose: ")

                if option == "1":
                    print("\nUsername:", user[0])
                    print("Free Fire UID:", user[2])
                    print("Game Name:", user[3])
                    print("Region:", user[4])

                elif option == "2":
                    break

                else:
                    print("Wrong Option")

        else:
            print("Wrong Username or Password")

    elif ch == "3":

        print("Bye")
        break

    else:

        print("Wrong Option")

conn.close()
