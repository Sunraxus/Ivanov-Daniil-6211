import os

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding

from methods.serialization_deserialization import KeySerialization
from methods.work_w_files import WorkFile


class SymmetricEncryption:
    """
    Provides methods for symmetric encryption and decryption.
    """
    
    @staticmethod
    def generate_symmetric_key() -> bytes:
        """
        Generate a symmetric key.

        Returns:
            bytes: Generated symmetric key.
        """
        return os.urandom(16)

    @staticmethod
    def encrypt_text(
        symmetric_key_path: str, text_file_path: str, encrypted_file_path: str
    ) -> bytes:
        """
        Encrypts text using symmetric encryption.

        Arguments:
            symmetric_key_path (str): Path to the file containing the symmetric key.
            text_file_path (str): Path to the file containing the plaintext.
            encrypted_file_path (str): Path to save the encrypted text.

        Returns:
            bytes: Encrypted text.
        """
        try:
            iv = os.urandom(8)
            symmetric_key = KeySerialization.load_symmetric_key(symmetric_key_path)
            plaintext = WorkFile.read_text_file(text_file_path)
            cipher = Cipher(algorithms.IDEA(symmetric_key), modes.CBC(iv))
            padder = padding.PKCS7(128).padder()
            padded_plaintext = (
                padder.update(plaintext.encode("utf-8")) + padder.finalize()
            )
            encryptor = cipher.encryptor()
            encrypted_text = (
                iv + encryptor.update(padded_plaintext) + encryptor.finalize()
            )
            WorkFile.write_bytes(encrypted_file_path, encrypted_text)
            return encrypted_text
        except Exception as e:
            print(f"An error occurred during encryption: {e}")

    @staticmethod
    def decrypt_text(
        symmetric_key_path: str, encrypted_file_path: str, decrypted_file_path: str
    ) -> str:
        """
        Decrypts encrypted text using symmetric encryption.

        Arguments:
            symmetric_key_path (str): Path to the file containing the symmetric key.
            encrypted_file_path (str): Path to the file containing the encrypted text.
            decrypted_file_path (str): Path to save the decrypted text.

        Returns:
            str: Decrypted text.
        """
        try:
            encrypted_data = WorkFile.read_bytes(encrypted_file_path)
            iv = encrypted_data[:8]
            ciphertext = encrypted_data[8:]
            symmetric_key = KeySerialization.load_symmetric_key(symmetric_key_path)
            cipher = Cipher(algorithms.IDEA(symmetric_key), modes.CBC(iv))
            decryptor = cipher.decryptor()
            padded_plaintext = decryptor.update(ciphertext) + decryptor.finalize()
            unpadder = padding.PKCS7(128).unpadder()
            plaintext = unpadder.update(padded_plaintext) + unpadder.finalize()
            decoded_text = plaintext.decode("utf-8")
            WorkFile.write_text_file(decrypted_file_path, decoded_text)
            return decoded_text
        except Exception as e:
            print(f"An error occurred during decryption: {e}")
            return ""

