# PHONEBOOK SYSTEM

def display_menu():
    print("Phonebook Application")
    print("1. Add Entry")
    print("2. Search Entry")
    print("3. Delete Entry")
    print("4. List All Entries")
    print("5. Exit")

def add_entry(phonebook):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    phonebook[name] = phone
    print(f"Entry added: {name} - {phone}")

def search_entry(phonebook):
    name = input("Enter name to search: ")
    if name in phonebook:
        print(f"Found entry: {name} - {phonebook[name]}")
    else:
        print("Entry not found.")

def delete_entry(phonebook):
    name = input("Enter name to delete: ")
    if name in phonebook:
        del phonebook[name]
        print(f"Entry deleted: {name}")
    else:
        print("Entry not found.")

def list_entries(phonebook):
    if phonebook:
        print("Phonebook Entries:")
        for name, phone in phonebook.items():
            print(f"{name} - {phone}")
    else:
        print("Phonebook is empty.")

def main():
    phonebook = {}
    while True:
        display_menu()
        choice = input("Choose an option (1-5): ")
        if choice == '1':
            add_entry(phonebook)
        elif choice == '2':
            search_entry(phonebook)
        elif choice == '3':
            delete_entry(phonebook)
        elif choice == '4':
            list_entries(phonebook)
        elif choice == '5':
            print("Exiting the Phonebook Application.")
            break
        else:
            print("Invalid choice. Please choose a valid option (1-5).")

if __name__ == "__main__":
    main()
