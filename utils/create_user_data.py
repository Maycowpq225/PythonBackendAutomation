import json
import random
import string
from datetime import date, timedelta


class CreateUserData:
    FIRST_NAMES = [
        "Lucas", "Ana", "Marcos", "Beatriz", "Felipe", "Maycow",
        "Rafael", "Larissa", "Gustavo", "Fernanda", "Bruno", "Juliana"
    ]

    LAST_NAMES = [
        "Silva", "Souza", "Oliveira", "Costa", "Pereira", "Rodrigues",
        "Almeida", "Nascimento", "Araujo", "Fernandes", "Carvalho"
    ]

    SPECIALTIES = [
        "Fisioterapia", "Nutrição", "Psicologia", "Odontologia", "Dermatologia",
        "Personal Trainer", "Oftalmologia", "Endocrinologia", "Pilates", "Estética"
    ]

    def __init__(self):
        first = random.choice(self.FIRST_NAMES)
        last = random.choice(self.LAST_NAMES)
        self.name = f"{first} {last}"
        domain = "@testmail.com"
        random_number = random.randint(0, 999)
        self.email = f"{first}.{last}{random_number}{domain}".lower()
        self.password = self._generate_valid_password()
        self.birthday = self._generate_valid_birthday()
        self.specialty = random.choice(self.SPECIALTIES)

    def _generate_valid_password(self):
        upper = random.choice(string.ascii_uppercase)
        lower = random.choice(string.ascii_lowercase)
        digit = random.choice(string.digits)
        symbol = random.choice("!@#$%")

        all_chars = string.ascii_letters + string.digits + "!@#$%"
        password = upper + lower + digit + symbol

        while len(password) < 10:
            password += random.choice(all_chars)

        return password

    def _generate_valid_birthday(self):
        today = date.today()
        maximum_birthday = today - timedelta(days=50 * 365) #gets 65 years in the past counting in days
        minimum_birthday = today - timedelta(days=18 * 365) #gets 18 years in the past counting in days
        difference_days = (minimum_birthday - maximum_birthday).days #gets the difference in days
        random_day_between_range = timedelta(days=random.randint(0, difference_days)) #gets a random date/day in the range
        random_birthday = maximum_birthday + random_day_between_range

        return random_birthday.isoformat()  # yyyy-MM-dd

    def to_json(self):
        return {
            "email": self.email,
            "password": self.password,
            "birthday": self.birthday,
            "name": self.name,
            "specialty": self.specialty
        }