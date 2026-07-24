import sqlite3
conn = sqlite3.connect("dropzone.db")
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, name TEXT, password TEXT)")
cursor.execute("CREATE TABLE IF NOT EXISTS joins(id INTEGER PRIMARY KEY, player TEXT, match_name TEXT)")
conn.commit()


def join_match(player, match_name):
    cursor.execute(
        "INSERT INTO joins(player, match_name) VALUES(?,?)",
        (player, match_name)
    )
    conn.commit()
    print("Match Join Successful")


def dashboard(name):
    while True:
        print("\n===== DropZone Dashboard =====")
        print("1. Tournament")
        print("2. Profile")
        print("3. Settings")
        print("4. Logout")

        op = input("Choose: ")

        if op == "1":
            print("\n===== Free Fire Tournament =====")
            print("1. Solo Match")
            print("2. Duo Match")
            print("3. Squad Match")
            print("4. High Kill Match")

            m = input("Choose Match: ")

            if m == "1":
                match = "Solo Match"
                print("\nEntry Fee: ₹10")
                print("Prize Pool: ₹500")
            elif m == "2":
                match = "Duo Match"
                print("\nEntry Fee: ₹20")
                print("Prize Pool: ₹1000")
            elif m == "3":
                match = "Squad Match"
                print("\nEntry Fee: ₹40")
                print("Prize Pool: ₹2000")
            elif m == "4":
                match = "High Kill Match"
                print("\nEntry Fee: ₹50")
                print("Prize Pool: ₹5000")
            else:
                print("Wrong Match")
                continue

            print("Players: 48")
            print("1. Join Match")

            j = input("Choose: ")

            if j == "1":
                join_match(name, match)

        elif op == "2":
            print("Profile:", name)

        elif op == "3":
            print("Settings Open")

        elif op == "4":
            print("Logout Done")
            break

        else:
            print("Wrong option")


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
        dashboard(name)
    else:
        print("Wrong Login")


elif choice == "3":
    print("Bye")

else:
    print("Wrong option")


conn.close()
