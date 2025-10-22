from faker import Faker
from Address import Address
from Name import Name
from random import choice, randint

fake = Faker()
# salespeople = []
# for i in range(10):
#     salespeople.append(Name())
#
# with open("customers.txt","w") as f:
#     for header in ["salesperson", "first", "last", "address", "city", "state", "zip", "phone", "email"]:
#         if header != "email":
#             f.write(header+",")
#         else:
#             f.write(header)
#     f.write("\n")
#     for i in range(1000):
#         saleseperson = choice(salespeople)
#         f.write(saleseperson.first+ " " + saleseperson.last+",")
#         name = Name()
#         f.write(name.first+",")
#         f.write(name.last+",")
#         address = Address()
#         f.write(address.street+",")
#         f.write(address.city+",")
#         f.write(address.state+",")
#         f.write(address.postal_code+",")
#         f.write(fake.phone_number()+",")
#         f.write(fake.email()+"\n")

with open("clients.txt", "w") as file:
    for i in range(300):
        file.write(fake.first_name()+",")
        file.write(fake.last_name()+",")
        file.write(fake.street_address()+",")
        file.write(fake.city()+",")
        file.write(fake.state()+",")
        file.write(fake.zipcode())
        file.write("\n")
