import json

from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.serialization import (
    load_pem_public_key,
    load_pem_private_key,
)


class KeySerialization:
    @staticmethod
    def save_symmetric_key(file_path: str, key: bytes) -> None:
        try:
            with open(file_path, "wb") as key_file:
                key_file.write(key)
        except Exception as error:
            print(f"An error occurred: {error}")

    @staticmethod
    def load_symmetric_key(file_path: str) -> bytes:
        try:
            with open(file_path, "rb") as key_file:
                symmetric_key = key_file.read()
                return symmetric_key
        except Exception as error:
            print(f"An error occurred: {error}")

    @staticmethod
    def save_asymmetric_public_key(file_path: str, public_key: rsa.RSAPublicKey) -> None:
        try:
            with open(file_path, "wb") as public_file:
                public_file.write(
                    public_key.public_bytes(
                        encoding=serialization.Encoding.PEM,
                        format=serialization.PublicFormat.SubjectPublicKeyInfo,
                    )
                )
        except Exception as error:
            print(f"An error occurred: {error}")

    @staticmethod
    def save_asymmetric_private_key(file_path: str, private_key: rsa.RSAPrivateKey) -> None:
        try:
            with open(file_path, "wb") as private_file:
                private_file.write(
                    private_key.private_bytes(
                        encoding=serialization.Encoding.PEM,
                        format=serialization.PrivateFormat.TraditionalOpenSSL,
                        encryption_algorithm=serialization.NoEncryption(),
                    )
                )
        except Exception as error:
            print(f"An error occurred: {error}")

    @staticmethod
    def load_asymmetric_public_key(file_path: str) -> rsa.RSAPublicKey:
        try:
            with open(file_path, "rb") as public_file:
                public_key_data = public_file.read()
            public_key = load_pem_public_key(public_key_data)
            return public_key
        except Exception as error:
            print(f"An error occurred: {error}")

    @staticmethod
    def load_asymmetric_private_key(file_path: str) -> rsa.RSAPrivateKey:
        try:
            with open(file_path, "rb") as private_file:
                private_key_data = private_file.read()
            private_key = load_pem_private_key(private_key_data, password=None)
            return private_key
        except Exception as error:
            print(f"An error occurred: {error}")
            return None