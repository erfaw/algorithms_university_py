import secrets

class Client:
    def __init__(self):
        """Makes a client for the Diffie-Hellman key exchange protocol."""
        self.private_key:int = None
        self.confirm_numbers = {
            "prime": None,
            "generator": None,
        }
    
    def generate_private_key(self):
        """
        Generates a private key which is a random number with any restriction.
        * Randomness: The private key should be a truly random number to ensure its security. In practice, this means using a cryptographically secure pseudo-random number generator or a hardware-based random number generator.
        * Large enough: The private key should be large enough to make it computationally infeasible for an attacker to guess or brute-force the value. A common guideline is to use a private key that is at least 256 bits (32 bytes) long.
        """
        return secrets.randbits(256)
