import sqlite3

conn = sqlite3.connect("dropzone.db")
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS joins(name TEXT, match TEXT)")
conn.commit()

name = input("Player Name: ")

while True:

    print("\n===== DropZone =====")
    print("1. Tournament")
    print("2. My Matches")
    print("3. Admin Panel")
    print("4. Logout")

    option = input("Choose: ")

    if option == "1":

        print("\n===== Tournament =====")
        print("1. Solo Match")
        print("2. Duo Match")
        print("3. Squad Match")
        print("4. High Kill Match")

        m = input("Select Match: ")

        if m == "1":
            match = "Solo Match"
        elif m == "2":
            match = "Duo Match"
        elif m == "3":
            match = "Squad Match"
        elif m == "4":
            match = "High Kill Match"
        else:
            match = "Wrong"

        if match != "Wrong":
            cursor.execute(
                "INSERT INTO joins VALUES(?,?)",
                (name, match)
            )
            conn.commit()
            print("Join Successful")

    elif option == "2":

        print("\n===== My Matches =====")

        cursor.execute(
            "SELECT match FROM joins WHERE name=?",
            (name,)
        )

        for x in cursor.fetchall():
            print(x[0])

    elif option == "3":

        print("\n===== Admin Panel =====")

        cursor.execute("SELECT * FROM joins")

        for x in cursor.fetchall():
            print(x[0], "-", x[1])

    elif option == "4":

        print("Logout Done")
        break

    else:

        print("Wrong Option")

conn.close()
