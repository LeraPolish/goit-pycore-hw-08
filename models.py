from datetime import datetime

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, name):
        super().__init__(name)

class Phone(Field):
    def __init__(self, number):
        self.validate(number)
        super().__init__(number)

    @staticmethod
    def validate(number):
        if not number.isdigit() or len(number) != 10:
            raise ValueError("Wrong format! Phone number must be 10 digits long.")

class Birthday(Field):
    def __init__(self, value):
        self.validate(value)
        self.date = datetime.strptime(value, "%d.%m.%Y").date()
        super().__init__(value)

    @staticmethod
    def validate(value):
        try:
            datetime.strptime(value, "%d.%m.%Y")
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, removed_phone):
        self.phones = [phone for phone in self.phones if phone.value != removed_phone]

    def edit_phone(self, old_phone, new_phone):
        for i, phone in enumerate(self.phones):
            if phone.value == old_phone:
                self.phones[i] = Phone(new_phone)
                return
        raise ValueError("Phone number not found.")

    def find_phone(self, this_phone):
        for phone in self.phones:
            if phone.value == this_phone:
                return phone
        return None

    def add_birthday(self, date):
        self.birthday = Birthday(date)

    def __str__(self):
        phones = '; '.join(p.value for p in self.phones)
        birthday = f", birthday: {self.birthday.value}" if self.birthday else ""
        return f"Contact name: {self.name.value}, phones: {phones}{birthday}"
