import argparse

from methods.crypto_system import CryptoSystem
from methods.work_w_files import WorkFile


def main():
    """
    Main function for running the hybrid cryptosystem.
    """
    
    parser = argparse.ArgumentParser(description="Hybrid Cryptosystem")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    gen_keys_parser = subparsers.add_parser(
        "generate_keys", help="Generate keys for hybrid cryptosystem"
    )

    encrypt_parser = subparsers.add_parser(
        "encrypt_data", help="Encrypt data using hybrid cryptosystem"
    )

    decrypt_parser = subparsers.add_parser(
        "decrypt_data", help="Decrypt data using hybrid cryptosystem"
    )

    args = parser.parse_args()

    settings = WorkFile.read_json_file("settings.json")

    match args.command:
        case "generate_keys":
            CryptoSystem.generate_keys(
                symmetric_key_path=settings["symmetric_key"],
                encrypted_symmetric_key_path=settings["encrypted_symmetric_key"],
                public_key_path=settings["public_key"],
                private_key_path=settings["secret_key"],
            )
        case "encrypt_data":
            CryptoSystem.encrypt_data(
                text_file_path=settings["initial_file"],
                private_key_path=settings["secret_key"],
                encrypted_symmetric_key_path=settings["encrypted_symmetric_key"],
                encrypted_file_path=settings["encrypted_file"],
                decrypted_symmetric_key_path=settings["decrypted_symmetric_key"],
            )
        case "decrypt_data":
            CryptoSystem.decrypt_data(
                encrypted_file_path=settings["encrypted_file"],
                private_key_path=settings["secret_key"],
                encrypted_symmetric_key_path=settings["encrypted_symmetric_key"],
                decrypted_file_path=settings["decrypted_file"],
                decrypted_symmetric_key_path=settings["decrypted_symmetric_key"],
            )
        case _:
            parser.print_help()


if __name__ == "__main__":
    main()

