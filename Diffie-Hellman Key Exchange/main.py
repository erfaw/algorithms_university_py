from client import Client

## make 2 person from Client class
person_1 = Client()
person_2 = Client()

## agree on big prime number
person_1.p = 11
person_2.p = person_1.p

## aggre on x number
person_1.x = 7
person_2.x = person_1.x

## pick exclusive numbers for each person
person_1.exclusive_number = 5
person_2.exclusive_number = 8

## Do calculation for discrete logarithm number and send it to each other
person_1.discrete_logarithm_cal_to_send = person_1.calculate_discrete_logarithm()
person_2.discrete_logarithm_cal_to_send = person_2.calculate_discrete_logarithm()

person_1.recieved_discrete_logarithm_number = person_2.discrete_logarithm_cal_to_send
person_2.recieved_discrete_logarithm_number = person_1.discrete_logarithm_cal_to_send

## Do calculation for result key for each person
person_1.result_key = person_1.calculate_result_key()
person_2.result_key = person_2.calculate_result_key()

print(f"this is result key for person_1:\n\t{person_1.result_key}")
print(f"this is result key for person_2:\n\t{person_2.result_key}")

