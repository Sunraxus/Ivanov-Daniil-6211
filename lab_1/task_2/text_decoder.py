import json

from constants2 import PATHS_2, KEY_2
from frequency_analysis import read_json_file


def replace_characters(text: str, key: dict) -> str:
    """
    Replace characters in the text using the provided key.
    Arguments:
        text (str): The text to be processed.
        key (dict): Dictionary representing the character replacement key.
        
    Returns:
        str: The text with characters replaced according to the key.
    """
    replaced_text = ""
    for char in text:
        if char in key:
            replaced_text += key[char]
        else:
            replaced_text += char
    return replaced_text


def process_text(file_paths: dict, key: dict) -> None:
    """
    Process the input text file using the provided key and write the decrypted text to the output file. 
    Arguments:
        file_paths (dict): Dictionary containing paths to input and output files.
        key (dict): Dictionary representing the character replacement key.
    """
    try:
        folder = file_paths.get("folder", "")
        input_file_path = file_paths.get("input_text2", "")
        output_file_path = file_paths.get("output_text2", "")

        if folder and input_file_path and output_file_path:
            input_file_path = f"{folder}/{input_file_path}"
            output_file_path = f"{folder}/{output_file_path}"

            with open(input_file_path, "r", encoding="utf-8") as input_file:
                text = input_file.read()

            decrypted_text = replace_characters(text, key)

            with open(output_file_path, "w", encoding="utf-8") as output_file:
                output_file.write(decrypted_text)

            print("Decryption completed successfully.")
        else:
            print("Error: Invalid paths data in path.json.")
    except FileNotFoundError:
        print(f"Error: File not found.")
    except Exception as e:
        print(f"Unexpected error occurred during decryption: {e}")


def process_files():
    """
    Read paths from the configuration file, process the input text file, and write the decrypted text to the output file.
    """
    paths_data = read_json_file(PATHS_2)

    if paths_data:
        process_text(paths_data, KEY_2)
    else:
        print("Error: Unable to read paths data from path.json.")


if __name__ == "__main__":
    process_files()

