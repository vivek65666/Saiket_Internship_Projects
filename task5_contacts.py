contacts = []

while True:
    print("\n===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        name = input("Enter Name: ")
        phone = input("Enter Phone: ")
        email = input("Enter Email: ")
        contacts.append({"name": name, "phone": phone, "email": email})
        print("Contact added successfully!")

    elif choice == "2":
        if len(contacts) == 0:
            print("No contacts found.")
        else:
            for contact in contacts:
                print(contact)

    elif choice == "3":
        search_name = input("Enter name to search: ")
        found = False
        for contact in contacts:
            if contact["name"].lower() == search_name.lower():
                print(contact)
                found = True
        if not found:
            print("Contact not found.")

    elif choice == "4":
        delete_name = input("Enter name to delete: ")
        contacts = [c for c in contacts if c["name"].lower() != delete_name.lower()]
        print("Contact deleted if it existed.")

    elif choice == "5":
        print("Exiting Contact Book...")
        break

    else:
        print("Invalid choice. Try again.")