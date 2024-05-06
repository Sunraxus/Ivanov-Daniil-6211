import json
import string

from constants1 import KEY_1, PATHS_1


def read_json_file(file_path: str) -> dict:
    """
    A function that allows you to read data from a JSON file.
    Arguments:
        file_path (str): The path to the JSON file.
    Returns:
        dict: A dictionary storing data from a JSON file.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return {}
    except Exception as e:
        print(f"Unexpected error occurred while reading file '{file_path}': {e}.")
        return {}


def caesar_cipher(text: str) -> str:
    """
    Function to apply Caesar cipher encryption to the given text.
    Arguments:
        text (str): The text to be encrypted.
    Returns:
        str: The encrypted text.
    """
    encrypted_text = "".join(KEY_1.get(char, char) for char in text)
    return encrypted_text


def process_text(input_file_path: str, output_file_path: str, key: dict) -> None:
    """
    Function for reading text from the input file, applying the Caesar cipher to this text and further
    writing to the output file.
    Arguments:
        input_file_path (str): Path to the input text file.
        output_file_path (str): The path to the output text file.
        key (dict): A dictionary representing the encryption key.
    """
    try:
        with open(input_file_path, "r", encoding="utf-8") as input_file:
            text = input_file.read()

        text = text.lower()
        text = text.translate(str.maketrans("", "", string.punctuation))

        encrypted_text = "".join(key.get(char, char) for char in text)

        with open(output_file_path, "w", encoding="utf-8") as output_file:
            output_file.write(encrypted_text)

        print("Encryption completed successfully.")
    except FileNotFoundError:
        print(f"Error: Input file '{input_file_path}' not found.")
    except Exception as e:
        print(f"Unexpected error occurred during encryption: {e}")


def process_files():
    """
    Function to read paths from the configuration file, process the input text file,
    and write the encrypted text to the output text file.
    """
    paths_data = read_json_file(PATHS_1)

    if paths_data:
        folder = paths_data.get("folder", "")
        input_file_path = paths_data.get("input_text1", "")
        output_file_path = paths_data.get("output_text1", "")

        if folder and input_file_path and output_file_path:
            input_file_path = f"{folder}/{input_file_path}"
            output_file_path = f"{folder}/{output_file_path}"
            process_text(input_file_path, output_file_path, KEY_1)
        else:
            print("Error: Invalid paths data in path.json.")
    else:
        print("Error: Unable to read paths data from path.json.")


if __name__ == "__main__":
    process_files()
