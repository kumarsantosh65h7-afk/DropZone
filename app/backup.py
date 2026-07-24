print("===== DropZone =====")
print("1. Home")
print("2. Profile")
print("3. Settings")
print("4. Exit")

choice = input("Option choose karo: ")

if choice == "1":
    print("Welcome to DropZone Home")

elif choice == "2":
    try:
        with open("data/profile.txt", "r") as file:
            name = file.read()
        print("Your Profile:", name)
    except:
        print("Profile nahi mili")

elif choice == "3":
    print("Settings open")

elif choice == "4":
    print("Bye! Thank you")

else:
    print("Wrong option")
