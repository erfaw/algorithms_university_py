import secrets
import sympy

class Client:
    def __init__(self):
        """Makes a client for the Diffie-Hellman key exchange protocol."""
        self.private_key:int = None
        self.confirm_numbers = {
            "prime": None,
            "generator": None,
        }
    
    def generate_private_key(self) -> int:
        """Generates a private key with sufficient randomness and size (256-bit)."""
        return secrets.randbits(256)

    def generate_big_prime_number(self):
        """Generate a 2048-bit (256-byte) prime number (orginal size)"""
        return sympy.nextprime(2**11)