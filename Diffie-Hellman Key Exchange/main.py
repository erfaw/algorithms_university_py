from client import Client
import subprocess; subprocess.call('cls', shell=True)

## make 2 person from Client class
person_1 = Client()
person_2 = Client()

## agree on big prime number
person_1.p = person_1.generate_big_prime_number()
person_2.p = person_1.p

## aggre on x number
person_1.x = person_1.generate_x_number()
person_2.x = person_1.x

## pick exclusive numbers for each person
person_1.exclusive_number = person_1.generate_exclusive_number()
person_2.exclusive_number = person_2.generate_exclusive_number()

## Do calculation for discrete logarithm number and send it to each other
person_1.discrete_logarithm_cal_to_send = person_1.calculate_discrete_logarithm()
print(f"this is dicrete logarithm calculated from person_1 to send person_2:\n\t{person_1.discrete_logarithm_cal_to_send}")
person_2.discrete_logarithm_cal_to_send = person_2.calculate_discrete_logarithm()
print(f"this is dicrete logarithm calculated from person_2 to send person_1:\n\t{person_2.discrete_logarithm_cal_to_send}")

person_1.recieved_discrete_logarithm_number = person_2.discrete_logarithm_cal_to_send
person_2.recieved_discrete_logarithm_number = person_1.discrete_logarithm_cal_to_send

## Do calculation for result key for each person
person_1.result_key = person_1.calculate_result_key()
print(f"this is result key of person_1:\n\t{person_1.result_key}")
person_2.result_key = person_2.calculate_result_key()
print(f"this is result key of person_2:\n\t{person_2.result_key}")

print()

