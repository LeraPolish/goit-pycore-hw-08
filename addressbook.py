from collections import UserDict
from datetime import datetime, timedelta
from models import Record

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name not in self.data:
            raise KeyError('Name not found')
        del self.data[name]

    def get_upcoming_birthdays(self, days=7):
        def find_next_weekday(start_date, weekday):
            days_ahead = weekday - start_date.weekday()
            if days_ahead <= 0:
                days_ahead += 7
            return start_date + timedelta(days=days_ahead)

        def adjust_for_weekend(birthday):
            if birthday.weekday() >= 5:
                return find_next_weekday(birthday, 0)
            return birthday

        upcoming_birthdays = []
        today = datetime.today().date()

        for record in self.data.values():
            if record.birthday:
                user_birthday = record.birthday.date
                next_birthday = user_birthday.replace(year=today.year)
                if next_birthday < today:
                    next_birthday = user_birthday.replace(year=today.year + 1)

                if 0 <= (next_birthday - today).days <= days:
                    next_birthday = adjust_for_weekend(next_birthday)
                    upcoming_birthdays.append({"name": record.name.value, "congratulation_date": next_birthday.strftime("%d.%m.%Y")})

        return upcoming_birthdays
