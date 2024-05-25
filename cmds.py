from utils import input_error
from models import Record

@input_error
def add_birthday(args, book):
    name, birthday = args
    record = book.find(name)
    if record:
        record.add_birthday(birthday)
        return f"Birthday {birthday} added to contact {name}."
    return f"No contact with name {name} found."

@input_error
def show_birthday(args, book):
    name = args[0]
    record = book.find(name)
    if record and record.birthday:
        return f"{name}'s birthday is on {record.birthday.value}"
    return f"No birthday information for {name}."

@input_error
def birthdays(book):
    upcoming_birthdays = book.get_upcoming_birthdays()
    if not upcoming_birthdays:
        return "No upcoming birthdays."
    result = "Upcoming birthdays:\n"
    result += "\n".join(f"{record['name']}: {record['congratulation_date']}" for record in upcoming_birthdays)
    return result

@input_error
def add_contact(args, book):
    name, phone = args
    record = book.find(name)
    if record:
        record.add_phone(phone)
        return f"Phone {phone} added to contact {name}."
    else:
        record = Record(name)
        record.add_phone(phone)
        book.add_record(record)
        return f"Contact {name} with phone {phone} added."

@input_error
def change_contact(args, book):
    name, new_phone = args
    record = book.find(name)
    if record:
        old_phone = record.phones[0].value
        record.edit_phone(old_phone, new_phone)
        return f"Phone number for {name} changed to {new_phone}."
    return f"No contact with name {name} found."

@input_error
def show_phone(args, book):
    name = args[0]
    record = book.find(name)
    if record and record.phones:
        phones = '; '.join(phone.value for phone in record.phones)
        return f"{name}'s phone numbers are: {phones}"
    return f"No phone numbers for {name} found."

@input_error
def show_all(book):
    if not book.data:
        return "No contacts found."
    result = "Contacts:\n"
    for name, record in book.data.items():
        result += str(record) + "\n"
    return result.strip()

@input_error
def parse_input(user_input):
    user_input = user_input.strip()
    cmd, *args = user_input.split()
    cmd = cmd.lower()
    return cmd, args
