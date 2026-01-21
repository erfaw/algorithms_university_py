import secrets
import sympy
import random

class Client:
    def __init__(self):
        """Makes a client for the Diffie-Hellman key exchange protocol."""
        self.p = None
        self.x = None
        self.exclusive_number = None
        self.discrete_logarithm_cal_to_send = None
        self.recieved_discrete_logarithm_number = None

        self.result_key = None

    def generate_big_prime_number(self):
        """Generate a 2048-bit (256-byte) prime number (orginal size)"""
        # Generate a large number of random values
        random_values = [secrets.randbits(256) for _ in range(1000)]

        # Filter out non-prime numbers
        prime_numbers = [val for val in random_values if sympy.isprime(val)]

        # Return a random choice of prime numbers
        return secrets.choice(prime_numbers)

    def generate_x_number(self):
        return random.randint(2, self.p-2)
    
    def generate_exclusive_number(self):
        return random.randint(2, self.p-2)
    
    def calculate_discrete_logarithm(self):
        return self.x**self.exclusive_number%self.p 
    
    def calculate_result_key(self):
        return (self.recieved_discrete_logarithm_number**self.exclusive_number)%self.p
        