import sqlite3

conn = sqlite3.connect("dropzone.db")
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS players(id INTEGER PRIMARY KEY, name TEXT, match_name TEXT)")
conn.commit()

def admin():
    while True:
        print("\n===== Admin Panel =====")
        print("1. View Players")
        print("2. Back")

        a = input("Choose: ")

        if a == "1":
            cursor.execute("SELECT * FROM players")
            data = cursor.fetchall()

            print("===== Players =====")

            if data:
                for p in data:
                    print(p[1], "-", p[2])
            else:
                print("No Players")

        elif a == "2":
            break

        else:
            print("Wrong option")


def dashboard(name):
    while True:
        print("\n===== DropZone Dashboard =====")
        print("1. Join Match")
        print("2. Admin Panel")
        print("3. Logout")

        op = input("Choose: ")

        if op == "1":
            print("1. Solo Match")
            print("2. Duo Match")

            m = input("Match: ")

            if m == "1":
                match = "Solo Match"
            else:
                match = "Duo Match"

            cursor.execute(
                "INSERT INTO players(name,match_name) VALUES(?,?)",
                (name,match)
            )
            conn.commit()

            print("Match Join Successful")

        elif op == "2":
            admin()

        elif op == "3":
            break

        else:
            print("Wrong option")


print("===== DropZone =====")
print("1. Login")

choice = input("Choose: ")

if choice == "1":
    name = input("Name: ")
    print("Welcome", name)
    dashboard(name)

conn.close()
