import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding

from work_w_files import WorkFile
from serialization_deserialization import KeySerialization


class SymmetricEncryption:
    @staticmethod
    def generate_symmetric_key() -> bytes:
        return os.urandom(16)

    @staticmethod
    def encrypt_text(symmetric_key_path: str, text_file_path: str, encrypted_file_path: str) -> bytes:
        try:
            iv = os.urandom(8) 
            symmetric_key = KeySerialization.load_symmetric_key(symmetric_key_path)
            plaintext = WorkFile.read_text_file(text_file_path)
            cipher = Cipher(algorithms.IDEA(symmetric_key), modes.CBC(iv))
            padder = padding.PKCS7(128).padder()
            padded_plaintext = padder.update(plaintext.encode('utf-8')) + padder.finalize()
            encryptor = cipher.encryptor()
            encrypted_text = iv + encryptor.update(padded_plaintext) + encryptor.finalize()
            WorkFile.write_bytes(encrypted_file_path, encrypted_text)
            return encrypted_text
        except Exception as e:
            print(f"An error occurred during encryption: {e}")

    @staticmethod
    def decrypt_text(symmetric_key_path: str, encrypted_file_path: str, decrypted_file_path: str) -> str:
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
            decoded_text = plaintext.decode('utf-8')
            WorkFile.write_text_file(decrypted_file_path, decoded_text)
            return decoded_text
        except Exception as e:
            print(f"An error occurred during decryption: {e}")
            return ""