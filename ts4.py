contacts = {}

def parse_input(command):
    parts = command.split()
    if len(parts) == 0:
        return None, []
    cmd = parts[0].lower()
    args = parts[1:]
    return cmd, args

def add_contact(name, phone):
    contacts[name] = phone
    return "Contact added."

def change_contact(name, new_phone):
    if name in contacts:
        contacts[name] = new_phone
        return "Contact updated."
    else:
        return "Contact not found."

def show_phone(name): 
    if name in contacts:
        return contacts[name]
    else:
        return "Contact not found."

def show_all():
    if contacts:
        return '\n'.join([f"{name}: {phone}" for name, phone in contacts.items()])
    else:
        return "No contacts found."

def main():
    print("Welcome to your assistant bot!")
    while True:
        command = input("Enter a command: ").strip()
        cmd, args = parse_input(command)
        if cmd == "exit" or cmd == "close":
            print("Good bye!")
            break
        elif cmd == "hello":
            print("How can I help you?")
        elif cmd == "add":
            if len(args) == 2:
                print(add_contact(args[0], args[1]))
            else:
                print("Invalid command format.")
        elif cmd == "change":
            if len(args) == 2:
                print(change_contact(args[0], args[1]))
            else:
                print("Invalid command format.")
        elif cmd == "phone":
            if len(args) == 1:
                print(show_phone(args[0]))
            else:
                print("Invalid command format.")
        elif cmd == "all":
            print(show_all())
        else:
            print("Unknown command.")

if __name__ == "__main__":
    main()
