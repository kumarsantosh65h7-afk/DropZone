import sqlite3

conn = sqlite3.connect("dropzone.db")
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS joins(name TEXT, match TEXT)")
cursor.execute("CREATE TABLE IF NOT EXISTS matches(name TEXT, fee TEXT, prize TEXT)")
conn.commit()

player = input("Player Name: ")

while True:

    print("\n===== DropZone =====")
    print("1. Join Match")
    print("2. My Matches")
    print("3. Admin Panel")
    print("4. Logout")

    option = input("Choose: ")

    if option == "1":

        print("\nAvailable Matches")

        cursor.execute("SELECT * FROM matches")
        data = cursor.fetchall()

        if data:
            for i, m in enumerate(data, 1):
                print(i, m[0], "Fee:", m[1], "Prize:", m[2])

            select = int(input("Select Match: "))
            match = data[select-1][0]

            cursor.execute(
                "INSERT INTO joins VALUES(?,?)",
                (player, match)
            )
            conn.commit()

            print("Match Join Successful")

        else:
            print("No Match Available")

    elif option == "2":

        print("\n===== My Matches =====")

        cursor.execute(
            "SELECT match FROM joins WHERE name=?",
            (player,)
        )

        for m in cursor.fetchall():
            print(m[0])


    elif option == "3":

        print("\n===== Admin Panel =====")
        print("1. Add Match")
        print("2. View Players")
        print("3. Back")

        a = input("Choose: ")

        if a == "1":

            name = input("Match Name: ")
            fee = input("Entry Fee: ")
            prize = input("Prize Pool: ")

            cursor.execute(
                "INSERT INTO matches VALUES(?,?,?)",
                (name, fee, prize)
            )

            conn.commit()
            print("Match Added")

        elif a == "2":

            cursor.execute("SELECT * FROM joins")

            for p in cursor.fetchall():
                print(p[0], "-", p[1])


    elif option == "4":

        print("Logout")
        break

    else:
        print("Wrong Option")

conn.close()
