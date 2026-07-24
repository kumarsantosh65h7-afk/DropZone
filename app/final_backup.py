print("===== DropZone =====")
print("1. Register")
print("2. Login")
print("3. Exit")

choice = input("Option choose karo: ")

if choice == "1":
    name = input("Name: ")
    password = input("Password: ")

    with open("data/user.txt", "w") as file:
        file.write(name + "\n")
        file.write(password + "\n")

    print("Account create ho gaya")

elif choice == "2":
    try:
        with open("data/user.txt", "r") as file:
            data = file.readlines()

        saved_name = data[0].strip()
        saved_password = data[1].strip()

        name = input("Name: ")
        password = input("Password: ")

        if name == saved_name and password == saved_password:
            print("Login Successful")
            print("Welcome", saved_name)

            while True:
                print("===== DropZone Dashboard =====")
                print("1. Home")
                print("2. My Profile")
                print("3. Settings")
                print("4. Logout")

                option = input("Choose: ")

                if option == "1":
                    print("Welcome to Home")

                elif option == "2":
                    print("Profile:", saved_name)

                elif option == "3":
                    print("===== Settings =====")
                    print("1. Account Info")
                    print("2. Change Name")
                    print("3. Back")

                    setting = input("Choose: ")

                    if setting == "1":
                        print("Account:", saved_name)
                    elif setting == "2":
                        print("Name change feature coming soon")
                    elif setting == "3":
                        print("Back")
                    else:
                        print("Wrong option")

                elif option == "4":
                    print("Logout Done")
                    break

                else:
                    print("Wrong option")

        else:
            print("Wrong Login")

    except:
        print("Pehle Register karo")

elif choice == "3":
    print("Bye")

else:
    print("Wrong option")
