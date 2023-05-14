contacts = {}

while True:
    print("\n---- Contact List ----")
    print("1. Show contact Name")
    print("2. Add contact")
    print("3. Remove contacts")
    print("4. Exit")

    choice = input("Enter your choice (s,a,r, or e): ")

    if choice == "a":
        name = input("Enter name: ")
        number = input("Enter phone number: ")
        contacts[name] = number
        print(f"{name} added to contacts")
    elif choice == "r":
        name = input("Enter name to remove: ")
        if name in contacts:
            del contacts[name]
            print(f"{name} removed from contacts")
        else:
            print(f"{name} not found in contacts")
    elif choice == "s":
        print("\n---- Contacts ----")
        for name, number in contacts.items():
            print(f"{name}: {number}")
    elif choice == "e":
        print("Exiting contact list...")
        break
    else:
        print("Invalid choice. Try again.")
