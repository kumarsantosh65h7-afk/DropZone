print("===== DropZone =====")

print("1. Register")
print("2. Login")
print("3. Exit")

choice = input("Choose: ")

if choice == "1":
    name = input("Name: ")
    password = input("Password: ")
    print("Account Created")
    print("अब Login करो")

elif choice == "2":
    name = input("Name: ")
    password = input("Password: ")

    print("Login Successful")
    print("Welcome", name)

    while True:
        print("\n===== DropZone Dashboard =====")
        print("1. Tournament")
        print("2. Profile")
        print("3. Logout")

        option = input("Choose: ")

        if option == "1":
            print("\nFree Fire Tournament")
            print("1. Solo Match")
            print("2. Duo Match")
            print("3. Squad Match")
            print("4. High Kill Match")

        elif option == "2":
            print("Profile:", name)

        elif option == "3":
            print("Logout Done")
            break

        else:
            print("Wrong Option")

elif choice == "3":
    print("Bye")

else:
    print("Wrong Option")
