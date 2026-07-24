print("===== DropZone =====")

print("1. Login")
print("2. Exit")

choice = input("Choose: ")

if choice == "1":

    name = input("Name: ")

    print("Login Successful")
    print("Welcome", name)

    while True:

        print("\n===== Dashboard =====")
        print("1. Tournament")
        print("2. Profile")
        print("3. Logout")

        option = input("Choose: ")

        if option == "1":

            print("\n===== Free Fire Tournament =====")
            print("1. Solo Match")
            print("2. Duo Match")
            print("3. Squad Match")
            print("4. High Kill Match")

            match = input("Select Match: ")

            if match == "1":
                print("Solo Match Join Successful")

            elif match == "2":
                print("Duo Match Join Successful")

            elif match == "3":
                print("Squad Match Join Successful")

            elif match == "4":
                print("High Kill Match Join Successful")

            else:
                print("Wrong Match")

        elif option == "2":

            print("Profile:", name)

        elif option == "3":

            print("Logout Done")
            break

        else:

            print("Wrong Option")

elif choice == "2":

    print("Bye")

else:

    print("Wrong Option")
