import json


class WorkFile:
    """
    Provides methods for reading and writing files.
    """
    
    @staticmethod
    def read_json_file(file_path: str) -> dict:
        """
        Read JSON data from a file.

        Arguments:
            file_path (str): Path to the JSON file.

        Returns:
            dict: Loaded JSON data.
        """
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                data = json.load(file)
            return data
        except FileNotFoundError:
            print(f"Error: File '{file_path}' not found.")
            return {}
        except Exception as e:
            print(
                f"An unexpected error occurred while reading file '{file_path}': {e}."
            )
            return {}

    @staticmethod
    def read_bytes(file_path: str) -> bytes:
        """
        Read bytes from a file.

        Arguments:
            file_path (str): Path to the file.

        Returns:
            bytes: Read bytes.
        """
        try:
            with open(file_path, "rb") as file:
                data = file.read()
            return data
        except FileNotFoundError:
            print(f"Error: File '{file_path}' not found.")
            return {}
        except Exception as e:
            print(
                f"An unexpected error occurred while reading file '{file_path}': {e}."
            )
            return {}

    @staticmethod
    def read_text_file(file_path: str) -> str:
        """
        Read text from a file.

        Arguments:
            file_path (str): Path to the file.

        Returns:
            str: Read text.
        """
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                data = file.read()
            return data
        except FileNotFoundError:
            print(f"Error: File '{file_path}' not found.")
            return {}
        except Exception as e:
            print(
                f"An unexpected error occurred while reading file '{file_path}': {e}."
            )
            return {}

    @staticmethod
    def write_bytes(file_path: str, text: bytes) -> None:
        """
        Write bytes to a file.

        Arguments:
            file_path (str): Path to the file.
            text (bytes): Bytes to write.
        """
        try:
            with open(file_path, "wb") as file:
                file.write(text)
        except FileNotFoundError:
            print(f"Error: File '{file_path}' not found.")
            return {}
        except Exception as e:
            print(
                f"An unexpected error occurred while reading file '{file_path}': {e}."
            )
            return {}

    @staticmethod
    def write_text_file(file_path: str, data: str) -> None:
        """
        Write text to a file.

        Arguments:
            file_path (str): Path to the file.
            data (str): Text to write.
        """
        try:
            with open(file_path, "a", encoding="UTF-8") as file:
                file.write(data)
        except FileNotFoundError:
            print(f"Error: File '{file_path}' not found.")
            return {}
        except Exception as e:
            print(
                f"An unexpected error occurred while reading file '{file_path}': {e}."
            )
            return {}

