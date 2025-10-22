from faker import Faker

class Address:
    def __init__(self):
        fake = Faker()
        lines = ["",""]
        while not "," in lines[1]:
            full_address = fake.address()
            lines = full_address.split('\n')
        self.street = lines[0].strip()
        second_line = lines[1].strip()
        self.city  = second_line.split(',')[0].strip()
        state_zip = second_line.split(',')[1].strip().split()
        self.state = state_zip[0].strip()
        self.postal_code = state_zip[1].strip()

    def print_address(self):
        print("street:", self.street)
        print("city:", self.city)
        print("state:", self.state)
        print("zip:", self.postal_code)

