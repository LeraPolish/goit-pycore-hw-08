from addressbook import AddressBook
from utils import save_data, load_data
from cmds import add_contact, change_contact, show_phone, show_all, add_birthday, show_birthday, birthdays, parse_input

def main():
    book = load_data()

    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        cmd, args = parse_input(user_input)

        if cmd in ["close", "exit"]:
            save_data(book)
            print("Good bye!")
            break
        elif cmd == "hello":
            print("How can I help you?")
        elif cmd == "add":
            if len(args) < 2:
                print("Invalid command format. Use: add [name] [phone]")
            else:
                print(add_contact(args, book))
        elif cmd == "change":
            if len(args) < 2:
                print("Invalid command format. Use: change [name] [new phone]")
            else:
                print(change_contact(args, book))
        elif cmd == "phone":
            if len(args) < 1:
                print("Invalid command format. Use: phone [name]")
            else:
                print(show_phone(args, book))
        elif cmd == "all":
            print(show_all(book))
        elif cmd == "add-birthday":
            if len(args) < 2:
                print("Invalid command format. Use: add-birthday [name] [birthday]")
            else:
                print(add_birthday(args, book))
        elif cmd == "show-birthday":
            if len(args) < 1:
                print("Invalid command format. Use: show-birthday [name]")
            else:
                print(show_birthday(args, book))
        elif cmd == "birthdays":
            print(birthdays(book))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
