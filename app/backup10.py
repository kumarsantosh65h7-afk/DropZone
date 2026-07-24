import sqlite3

conn = sqlite3.connect("dropzone.db")
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, name TEXT, password TEXT)")
conn.commit()

def dashboard(name):
    while True:
        print("\n===== DropZone Dashboard =====")
        print("1. Tournament")
        print("2. Profile")
        print("3. Settings")
        print("4. Logout")

        op = input("Choose: ")

        if op == "1":
            print("\n===== Matches =====")
            print("1. Solo Match")
            print("2. Duo Match")
            print("3. Squad Match")
            print("4. High Kill Match")

            m = input("Choose Match: ")

            if m == "1":
