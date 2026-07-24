import sqlite3

conn = sqlite3.connect("dropzone.db")
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS users(username TEXT,password TEXT,uid TEXT,game TEXT,region TEXT)")
cursor.execute("CREATE TABLE IF NOT EXISTS matches(username TEXT,match_type TEXT)")
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

        cursor.execute("INSERT INTO users VALUES(?,?,?,?,?)",(u,p,uid,game,reg))
        conn.commit()
        print("Account Created")

    elif ch == "2":
        u = input("Username: ")
        p = input("Password: ")

        cursor.execute("SELECT * FROM users WHERE username=? AND password=?",(u,p))
        user = cursor.fetchone()

        if user:
            print("Login Successful")

            while True:
                print("\n===== Dashboard =====")
                print("1. Profile")
                print("2. Join Tournament")
                print("3. My Matches")
                print("4. Logout")

                op = input("Choose: ")

                if op == "1":
                    print("Username:",user[0])
                    print("UID:",user[2])
                    print("Game:",user[3])
                    print("Region:",user[4])

                elif op == "2":
                    print("1. Solo")
                    print("2. Duo")
                    print("3. Squad")

                    m = input("Select: ")

                    if m == "1":
                        mt = "Solo"
                    elif m == "2":
                        mt = "Duo"
                    elif m == "3":
                        mt = "Squad"
                    else:
                        mt = ""

                    if mt:
                        cursor.execute("INSERT INTO matches VALUES(?,?)",(u,mt))
                        conn.commit()
                        print("Joined",mt)

                elif op == "3":
                    cursor.execute("SELECT match_type FROM matches WHERE username=?",(u,))
                    print("My Matches:")
                    for x in cursor.fetchall():
                        print(x[0])

                elif op == "4":
                    print("Logout Successful")
                    break

        else:
            print("Wrong Login")

    elif ch == "3":
        print("Bye")
        break

    else:
        print("Wrong Option")

conn.close()
