import json
import string

from constants1 import ALPHABET, SHIFT, PATHS_1


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


def caesar_cipher(text: str, shift: int) -> str:
    """
    Function to apply Caesar cipher encryption to the given text.
    Arguments:
        text (str): The text to be encrypted.
        shift (int): The shift value for the Caesar cipher.
    Returns:
        str: The encrypted text.
    """
    encrypted_text = ""
    text = text.upper()
    for i in text:
        if i.isalpha():
                index = ALPHABET.index(i)
                encrypted_text += ALPHABET[(index + shift) % len(ALPHABET)]
        else:
            encrypted_text += i
    return encrypted_text


def process_text(input_file_path: str, output_file_path: str) -> None:
    """
    Function for reading text from the input file, applying the Caesar cipher to this text, and further
    writing to the output file.
    Arguments:
        input_file_path (str): Path to the input text file.
        output_file_path (str): The path to the output text file.
    """
    try:
        with open(input_file_path, "r", encoding="utf-8") as input_file:
            text = input_file.read()

        encrypted_text = caesar_cipher(text, SHIFT)

        with open(output_file_path, "w", encoding="utf-8") as output_file:
            output_file.write(encrypted_text)

        print("Encryption completed successfully.")
    except FileNotFoundError:
        print(f"Error: Input file '{input_file_path}' not found.")
    except Exception as e:
        print(f"Unexpected error occurred during encryption: {e}")


def process_files(folder: str, input_file_name: str, output_file_name: str) -> None:
    """
    Function to process the input text file, and write the encrypted text to the output text file.
    Arguments:
        folder (str): Path to the folder containing input and output text files.
        input_file_name (str): Name of the input text file.
        output_file_name (str): Name of the output text file.
    """
    try:
        input_file_path = f"{folder}/{input_file_name}"
        output_file_path = f"{folder}/{output_file_name}"
        process_text(input_file_path, output_file_path)
    except Exception as e:
        print(f"An error occurred while processing files: {e}")


def main() -> None:
    """
    Main function to read paths from the configuration file, and process the input text file.
    """
    paths_data = read_json_file(PATHS_1)

    if paths_data:
        folder = paths_data.get("folder", "")
        input_file_name = paths_data.get("input_text1", "")
        output_file_name = paths_data.get("output_text1", "")

        if folder and input_file_name and output_file_name:
            process_files(folder, input_file_name, output_file_name)
        else:
            print("Error: Invalid paths data in path.json.")
    else:
        print("Error: Unable to read paths data from path.json.")


if __name__ == "__main__":
    main()

