import json
import string
from constants1 import KEY1, PATHS1

def read_json_file(file_path: str) -> dict:
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return {}
    except Exception as e:
        print(f"An unexpected error occurred while reading file '{file_path}': {e}.")
        return {}

def caesar_cipher(text: str, shift: int) -> str:
    alph = string.ascii_lowercase
    shifted_alph = alph[shift:] + alph[:shift]
    table = str.maketrans(alph, shifted_alph)
    return text.translate(table)

def process_text(input_file_path: str, output_file_path: str, key: dict) -> None:
    try:
        with open(input_file_path, "r", encoding="utf-8") as input_file:
            text = input_file.read()

        text = text.lower()
        text = text.translate(str.maketrans('', '', string.punctuation))

        encrypted_text = "".join(key.get(char, char) for char in text)

        with open(output_file_path, "w", encoding="utf-8") as output_file:
            output_file.write(encrypted_text)
        
        print("Encryption completed successfully.")
    except FileNotFoundError:
        print(f"Error: Input file '{input_file_path}' not found.")
    except Exception as e:
        print(f"An unexpected error occurred during encryption: {e}")

def process_files():
    paths_data = read_json_file(PATHS)

    if paths_data:
        folder = paths_data.get("folder", "")
        input_file_path = paths_data.get("input_text1", "")
        output_file_path = paths_data.get("output_text1", "")

        if folder and input_file_path and output_file_path:
            input_file_path = f"{folder}/{input_file_path}"
            output_file_path = f"{folder}/{output_file_path}"
            process_text(input_file_path, output_file_path, KEY)
        else:
            print("Error: Invalid paths data in path.json.")
    else:
        print("Error: Unable to read paths data from path.json.")


if __name__ == "__main__":
    process_files()
