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
                print("\n===== DropZone Dashboard =====")
                print("1. Tournament")
                print("2. My Profile")
                print("3. Settings")
                print("4. Logout")

                option = input("Choose: ")

                if option == "1":
                    print("\n===== Matches =====")
                    print("1. Solo Match")
                    print("2. Duo Match")
                    print("3. Squad Match")
                    print("4. High Kill Match")

                    match = input("Choose Match: ")

                    if match == "1":
                        print("\n🔥 Solo Match")
                        print("Entry Fee: ₹10")
                        print("Prize Pool: ₹500")
                        print("Players: 48")
                        print("1. Join Match")

                    elif match == "2":
                        print("\n🔥 Duo Match")
                        print("Entry Fee: ₹20")
                        print("Prize Pool: ₹1000")
                        print("Players: 48")
                        print("1. Join Match")

                    elif match == "3":
                        print("\n🔥 Squad Match")
                        print("Entry Fee: ₹40")
                        print("Prize Pool: ₹2000")
                        print("Players: 48")
                        print("1. Join Match")

                    elif match == "4":
                        print("\n🔥 High Kill Match")
                        print("Entry Fee: ₹50")
                        print("Prize Pool: ₹5000")
                        print("Players: 48")
                        print("1. Join Match")

                    else:
                        print("Wrong Match")

                elif option == "2":
                    print("Profile:", saved_name)

                elif option == "3":
                    print("Settings Open")

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
