class Client:
    def __init__(self):
        """Makes a client for the Diffie-Hellman key exchange protocol."""
        self.private_key = None
        self.confirm_numbers = {
            "prime": None,
            "generator": None,
        }
        