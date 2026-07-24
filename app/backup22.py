import sqlite3

conn = sqlite3.connect("dropzone.db")
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS wallet(name TEXT, balance INTEGER)")
cursor.execute("CREATE TABLE IF NOT EXISTS joins(name TEXT, match TEXT)")
conn.commit()

name = input("Player Name: ")

cursor.execute("SELECT * FROM wallet WHERE name=?", (name,))
if cursor.fetchone() is None:
    cursor.execute("INSERT INTO wallet VALUES(?,?)", (name, 0))
    conn.commit()

while True:
    print("===== DropZone =====")
    print("1. Wallet")
    print("2. Join Match")
    print("3. My Matches")
    print("4. Logout")

    choice = input("Choose: ")

    if choice == "1":
        cursor.execute("SELECT balance FROM wallet WHERE name=?", (name,))
        bal = cursor.fetchone()[0]
        print("Balance:", bal)

        add = input("Add money demo y/n: ")
        if add == "y":
            amount = int(input("Amount: "))
            cursor.execute(
                "UPDATE wallet SET balance=? WHERE name=?",
                (bal + amount, name)
            )
            conn.commit()
            print("Added")

    elif choice == "2":
        print("1 Solo")
        print("2 Duo")
        print("3 Squad")

        m = input("Match: ")

        if m == "1":
            match = "Solo"
        elif m == "2":
            match = "Duo"
        elif m == "3":
            match = "Squad"
        else:
            match = "Wrong"

        if match != "Wrong":
            cursor.execute(
                "INSERT INTO joins VALUES(?,?)",
                (name, match)
            )
            conn.commit()
            print("Joined", match)

    elif choice == "3":
        cursor.execute(
            "SELECT match FROM joins WHERE name=?",
            (name,)
        )

        print("My Matches:")
        for x in cursor.fetchall():
            print(x[0])

    elif choice == "4":
        print("Logout")
        break

    else:
        print("Wrong")

conn.close()
