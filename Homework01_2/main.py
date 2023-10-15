def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    try:
        name, phone = args
        contacts[name] = phone
        return "Contact added."
    except:
        return "Invalid command."

def change_contact(args, contacts):
    try:
        name, phone = args
        if name in contacts.keys():
            contacts[name] = phone
            return "Contact updated."
        else:
            return "Name doesn't find."
    except:
        return "Invalid command."

def show_all(args, contacts):
    res = ''
    for contact, phone_number in contacts.items():
        res = (f"{contact} : {phone_number}") if not res else res + '\n' + (f"{contact} : {phone_number}")
    return res    

def show_phone(args, contacts):
        name = args[0]
        if name in contacts.keys():
            return contacts[name]
        else:
            return "Didn't find"

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        if user_input:
            command, *args = parse_input(user_input)

            if command in ["close", "exit"]:
                print("Good bye!")
                break
            elif command == "hello":
                print("How can I help you?")
            elif command == "add":
                print(add_contact(args, contacts))
            elif command == "change":
                print(change_contact(args, contacts))
            elif command == "all":
                print(show_all(args, contacts))
            elif command == "phone":
                print(show_phone(args, contacts))
            else:
                print("Invalid command.")
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()