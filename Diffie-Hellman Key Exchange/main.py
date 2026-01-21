from client import Client

## make 2 person from Client class
person_1 = Client()
person_2 = Client()

## make and assign private key for each person
person_1.private_key = person_1.generate_private_key()
person_2.private_key = person_2.generate_private_key()

## agree on big prime number
person_1.confirm_numbers["prime"] = person_1.generate_big_prime_number()
person_2.confirm_numbers["prime"] = person_1.confirm_numbers["prime"]


