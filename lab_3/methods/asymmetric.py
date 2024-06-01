import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.asymmetric import padding as asym_padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa

from work_w_files import WorkFile
from serialization_deserialization import KeySerialization


class AsymmetricEncryption:
    @staticmethod
    def generate_asymmetric_keys() -> tuple[rsa.RSAPublicKey, rsa.RSAPrivateKey]:
        try:
            private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
            public_key = private_key.public_key()
            return public_key, private_key
        except Exception as e:
            print(f"An error occurred during key generation: {e}")

    @staticmethod
    def encrypt_symmetric_key(public_key_path: str, symmetric_key_path: str, encrypted_symmetric_key_path: str) -> None:
        try:
            symmetric_key = KeySerialization.load_symmetric_key(symmetric_key_path)
            public_key = KeySerialization.load_asymmetric_public_key(public_key_path)
            encrypted_key = public_key.encrypt(
                symmetric_key,
                asym_padding.OAEP(
                    mgf=asym_padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None,
                ),
            )
            WorkFile.write_bytes(encrypted_symmetric_key_path, encrypted_key)
        except Exception as e:
            print(f"An error occurred during symmetric key encryption: {e}")

    @staticmethod
    def decrypt_symmetric_key(encrypted_symmetric_key_path: str, private_key_path: str, decrypted_symmetric_key_path: str) -> bytes:
        try:
            encrypted_sym_key = WorkFile.read_bytes(encrypted_symmetric_key_path)
            private_key = KeySerialization.load_asymmetric_private_key(private_key_path)
            decrypted_key = private_key.decrypt(
                encrypted_sym_key,
                asym_padding.OAEP(
                    mgf=asym_padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None,
                ),
            )
            WorkFile.write_bytes(decrypted_symmetric_key_path, decrypted_key)
            return decrypted_key
        except Exception as e:
            print(f"An error occurred during symmetric key decryption: {e}")
            return b""