contacts = {}

while True:
    print("\n1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. Display Contacts")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")

        contacts[name] = phone

        print("Contact added")

    elif choice == "2":
        name = input("Enter name: ")

        if name in contacts:
            print("Phone:", contacts[name])
        else:
            print("Contact not found")

    elif choice == "3":
        name = input("Enter name: ")

        if name in contacts:
            del contacts[name]
            print("Contact deleted")
        else:
            print("Contact not found")

    elif choice == "4":
        if len(contacts) == 0:
            print("No contacts available")
        else:
            for name, phone in contacts.items():
                print(name, ":", phone)

    elif choice == "5":
        print("Exiting...")
        break

    else:
        print("Invalid choice")