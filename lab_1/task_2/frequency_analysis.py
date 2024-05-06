import json
from constants2 import PATHS2

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

def character_frequency(text: str) -> dict:
    
    freq_dict = {}
    total_chars = len(text)
    for char in text:
        if char in freq_dict:
            freq_dict[char] += 1
        else:
            freq_dict[char] = 1
            
    for char, freq in freq_dict.items():
        freq_dict[char] = freq / total_chars

    return freq_dict

def analyze_text(file_path: str) -> dict:
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            text = file.read()
        freq_dict = character_frequency(text)       
        return freq_dict
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return {}
    except Exception as e:
        print(f"An unexpected error occurred while analyzing text: {e}.")
        return {}

def analyze_text_from_json():
    paths_data = read_json_file(PATHS2)

    if paths_data:
        folder = paths_data.get("folder", "")
        input_file_path = paths_data.get("input_text2", "")

        if folder and input_file_path:
            input_file_path = f"{folder}/{input_file_path}"
            freq_dict = analyze_text(input_file_path)

            if freq_dict:
                print("Character frequency analysis (ratio of total characters):")
                for char, freq in freq_dict.items():
                    print(f"Character '{char}': {freq:.7f}")
            else:
                print("Error: Failed to analyze text.")
        else:
            print("Error: Invalid paths data in path.json.")
    else:
        print("Error: Unable to read paths data from path.json.")
        
        
if __name__ == "__main__":
    analyze_text_from_json()
