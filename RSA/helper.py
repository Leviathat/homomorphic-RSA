from lightphe import LightPHE, Ciphertext
from typing import Any


class CryptoHelper:
    _alg = "RSA"

    def __init__(self) -> None:
        self.cs = LightPHE(algorithm_name=self._alg)
    
    def encrypt(self, message: int) -> Any:
        return self.cs.encrypt(plaintext = message).value
    
    def decrypt(self, message: int) -> Any:
        ciphertext = Ciphertext(value=message, 
                        algorithm_name=self._alg,
                        keys=self.cs.cs.keys)
        
        return self.cs.decrypt(ciphertext = ciphertext)
    
    def generate_keys(self):
        keys = self.cs.cs.keys
        
        with open(".env", "w") as f:
            f.write(f"PUBLIC_KEY={keys['public_key']['n']}\n")
            f.write(f"PRIVATE_KEY={keys['private_key']['d']}\n")
            f.write(f"EVALUATION_KEY={keys['public_key']['e']}\n")

    def __enter__(self):
        self.generate_keys()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting")

ch = CryptoHelper()

if __name__ == "__main__":
    ch.generate_keys()