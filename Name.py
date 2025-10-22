from faker import Faker


class Name:
    def __init__(self):
        fake = Faker()
        self.first = fake.first_name()
        self.last = fake.last_name()