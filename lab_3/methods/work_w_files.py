import json


class WorkFile:
    @staticmethod
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
        
    @staticmethod
    def read_bytes(file_path: str) -> bytes:
        try:
            with open(file_path, "rb") as file:
                data = file.read()
            return data
        except FileNotFoundError:   
            print(f"Error: File '{file_path}' not found.")
            return {}
        except Exception as e:
            print(f"An unexpected error occurred while reading file '{file_path}': {e}.")
            return {}

    @staticmethod
    def read_text_file(file_path: str) -> str:
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                data = file.read()
            return data
        except FileNotFoundError:   
            print(f"Error: File '{file_path}' not found.")
            return {}
        except Exception as e:
            print(f"An unexpected error occurred while reading file '{file_path}': {e}.")
            return {}
    
    @staticmethod
    def write_bytes(file_path: str, text: bytes) -> None:
        try:
            with open(file_path, 'wb') as file:
                file.write(text)
        except FileNotFoundError:   
            print(f"Error: File '{file_path}' not found.")
            return {}
        except Exception as e:
            print(f"An unexpected error occurred while reading file '{file_path}': {e}.")
            return {}

    @staticmethod
    def write_text_file(file_path: str, data: str) -> None:
        try:
            with open(file_path, "a", encoding='UTF-8') as file:
                file.write(data)
        except FileNotFoundError:   
            print(f"Error: File '{file_path}' not found.")
            return {}
        except Exception as e:
            print(f"An unexpected error occurred while reading file '{file_path}': {e}.")
            return {}