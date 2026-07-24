import sqlite3

conn = sqlite3.connect("dropzone.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
username TEXT,
password TEXT
)
""")

conn.commit()

while True:

    print("\n===== DropZone =====")
    print("1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Choose: ")

    if choice == "1":

        username = input("Username: ")
        password = input("Password: ")

        cursor.execute(
            "INSERT INTO users VALUES(?,?)",
            (username, password)
        )

        conn.commit()

        print("Account Created")

    elif choice == "2":

        username = input("Username: ")
        password = input("Password: ")

        cursor.execute(
            "SELECT * FROM users WHERE username=? AND password=?",
            (username, password)
        )

        user = cursor.fetchone()

        if user:
            print("Login Successful")
            print("Welcome", username)

            while True:
                print("\n===== Dashboard =====")
                print("1. Profile")
                print("2. Logout")

                option = input("Choose: ")

                if option == "1":
                    print("Username:", username)

                elif option == "2":
                    break

        else:
            print("Wrong Username or Password")

    elif choice == "3":

        print("Bye")
        break

    else:

        print("Wrong Option")

conn.close()
