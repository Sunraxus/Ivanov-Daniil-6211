from methods.symmetric import SymmetricEncryption
from methods.asymmetric import AsymmetricEncryption
from methods.serialization_deserialization import KeySerialization


class CryptoSystem:
    """
    Provides methods for key generation, data encryption, and decryption using symmetric and asymmetric encryption.
    """
    
    @staticmethod
    def generate_keys(
        symmetric_key_path: str,
        encrypted_symmetric_key_path: str,
        public_key_path: str,
        private_key_path: str,
    ) -> None:
        """
        Generate symmetric and asymmetric keys, and encrypt the symmetric key.

        Arguments:
            symmetric_key_path (str): Path to save the generated symmetric key.
            encrypted_symmetric_key_path (str): Path to save the encrypted symmetric key.
            public_key_path (str): Path to save the generated RSA public key.
            private_key_path (str): Path to save the generated RSA private key.
        """
        try:
            symmetric_key = SymmetricEncryption.generate_symmetric_key()
            KeySerialization.save_symmetric_key(symmetric_key_path, symmetric_key)

            public_key, private_key = AsymmetricEncryption.generate_asymmetric_keys()

            KeySerialization.save_asymmetric_public_key(public_key_path, public_key)
            KeySerialization.save_asymmetric_private_key(private_key_path, private_key)

            AsymmetricEncryption.encrypt_symmetric_key(
                public_key_path, symmetric_key_path, encrypted_symmetric_key_path
            )

        except Exception as e:
            print(f"An error occurred during key generation: {e}")

    @staticmethod
    def encrypt_data(
        text_file_path: str,
        private_key_path: str,
        encrypted_symmetric_key_path: str,
        encrypted_file_path: str,
        decrypted_symmetric_key_path: str,
    ) -> None:
        """
        Encrypts data using symmetric encryption and encrypts the symmetric key using asymmetric encryption.

        Arguments:
            text_file_path (str): Path to the file containing the plaintext data.
            private_key_path (str): Path to the RSA private key used for symmetric key decryption.
            encrypted_symmetric_key_path (str): Path to the encrypted symmetric key file.
            encrypted_file_path (str): Path to save the encrypted data.
            decrypted_symmetric_key_path (str): Path to save the decrypted symmetric key.
        """
        try:
            AsymmetricEncryption.decrypt_symmetric_key(
                encrypted_symmetric_key_path,
                private_key_path,
                decrypted_symmetric_key_path,
            )

            SymmetricEncryption.encrypt_text(
                decrypted_symmetric_key_path, text_file_path, encrypted_file_path
            )

        except Exception as e:
            print(f"An error occurred during data encryption: {e}")

    @staticmethod
    def decrypt_data(
        encrypted_file_path: str,
        private_key_path: str,
        encrypted_symmetric_key_path: str,
        decrypted_file_path: str,
        decrypted_symmetric_key_path: str,
    ) -> None:
        """
        Decrypts data using symmetric encryption and decrypts the symmetric key using asymmetric encryption.

        Arguments:
            encrypted_file_path (str): Path to the file containing the encrypted data.
            private_key_path (str): Path to the RSA private key used for symmetric key decryption.
            encrypted_symmetric_key_path (str): Path to the encrypted symmetric key file.
            decrypted_file_path (str): Path to save the decrypted data.
            decrypted_symmetric_key_path (str): Path to save the decrypted symmetric key.
        """
        try:
            AsymmetricEncryption.decrypt_symmetric_key(
                encrypted_symmetric_key_path,
                private_key_path,
                decrypted_symmetric_key_path,
            )

            SymmetricEncryption.decrypt_text(
                decrypted_symmetric_key_path, encrypted_file_path, decrypted_file_path
            )

        except Exception as e:
            print(f"An error occurred during data decryption: {e}")

