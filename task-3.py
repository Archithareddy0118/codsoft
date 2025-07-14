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
        contacts[name] = 