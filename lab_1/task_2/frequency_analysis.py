import json

from collections import Counter

from constants2 import PATHS_2


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


def character_frequency(text: str) -> dict:
    """
    Calculate the frequency of each character in the given text.
    Arguments:
        text (str): The input text.
    Returns:
        dict: A dictionary containing the frequency of each character as a ratio of total characters.
    """
    freq_dict = Counter(text)
    total_chars = len(text)

    for char, freq in freq_dict.items():
        freq_dict[char] = freq / total_chars

    return freq_dict


def analyze_text(file_path: str) -> dict:
    """
    Analyze the frequency of characters in the text file.
    Arguments:
        file_path (str): Path to the text file.
    Returns:
        dict: A dictionary containing the frequency of each character as a ratio of total characters.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            text = file.read()
        freq_dict = character_frequency(text)
        return freq_dict
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return {}
    except Exception as e:
        print(f"Unexpected error occurred while analyzing text: {e}.")
        return {}


def analyze_text_from_json():
    """
    Analyze the frequency of characters in the text file specified in the JSON configuration file.
    """
    paths_data = read_json_file(PATHS_2)

    if not paths_data:
        print("Error: Unable to read paths data from path.json.")
        return

    folder = paths_data.get("folder", "")
    input_file_path = paths_data.get("input_text2", "")

    if not folder or not input_file_path:
        print("Error: Invalid paths data in path.json.")
        return

    input_file_path = f"{folder}/{input_file_path}"

    try:
        freq_dict = analyze_text(input_file_path)
        if freq_dict:
            print("Character frequency analysis (ratio of total characters):")
            for char, freq in freq_dict.items():
                print(f"Character '{char}': {freq:.7f}")
        else:
            print("Error: Failed to analyze text.")
    except Exception as e:
        print(f"Unexpected error occurred while analyzing text: {e}.")


if __name__ == "__main__":
    analyze_text_from_json()

