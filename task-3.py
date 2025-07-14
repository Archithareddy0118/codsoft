contacts = {}

def add_contact():
    name = input("Enter name: ")
    if name in contacts:
        print("Contact already exists.")
    else:
        phone = input("Enter phone number: ")
        contacts[name] = phone
        print("Contact added.")

def view_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        print("\nAll Contacts:")
        for name, phone in contacts.items():
            print(f"{name}: {phone}")

def delete_contact():
    name = input("Enter name to delete: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted.")
    else:
        print("Contact not found.")

def search_contact():
    name = input("Enter name to search: ")
    if name in contacts:
        print(f"{name}: {contacts[name]}")
    else:
        print("Contact not found.")

def update_contact():
    name = input("Enter name to update: ")
    if name in contacts:
        new_number = input("Enter new phone number: ")
        contacts[name] = new_number
        print("Contact updated.")
    else:
        print("Contact not found.")

def menu():
    while True:
        print("\n--- Contact Book ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Delete Contact")
        print("4. Search Contact")
        print("5. Update Contact")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            delete_contact()
        elif choice == "4":
            search_contact()
        elif choice == "5":
            update_contact()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

menu()