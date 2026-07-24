import sqlite3
conn = sqlite3.connect("dropzone.db")
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS joins(name TEXT, match TEXT)")
conn.commit()

print("===== DropZone =====")
name = input("Player Name: ")

while True:

    print("\n===== Dashboard =====")
print("1. Tournament")
print("2. My Matches")
print("3. Admin Panel")
print("4. Logout")
    option = input("Choose: ")

    if option == "1":

        print("\nFree Fire Tournament")
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

            print("Join Successful:", match)

        else:
            print("Wrong Match")

    elif option == "2":

        print("\n===== My Matches =====")

        cursor.execute(
            "SELECT match FROM joins WHERE name=?",
            (name,)
        )

        data = cursor.fetchall()

        for x in data:
            print(x[0])

    elif option == "3":

        print("Logout")
        break

    else:

        print("Wrong Option")

conn.close()
