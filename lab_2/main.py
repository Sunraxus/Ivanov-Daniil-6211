from math import sqrt
from scipy.special import erfc

from constants import SEQUENCE_CPP, SEQUENCE_JAVA, BLOCK_SIZE, PI_VALUES


def read_txt(file_name):
    try:
        with open(file_name, 'r') as file:
            text = file.read()
        return text
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
        return None
    except Exception as e:
        print(f"Unexpected error occurred while reading file '{file_name}': {e}.")
        return None
    
    
def frequency_bitwise_test(sequence: str) -> float:
    try:
        N = len(sequence)
        S = (sequence.count("1") - sequence.count("0")) / sqrt(N)
        P = erfc(abs(S) / sqrt(2))
        return P
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def consecutive_bits_test(sequence: str) -> float:
    try:
        N = len(sequence)
        Z = sequence.count("1") / N
        if abs(Z - 0.5) >= 2 / sqrt(N):
            return 0
        else:
            V = sum(1 if sequence[i] != sequence[i + 1] else 0 for i in range(N - 1))
            P = erfc((abs(V - 2 * N * Z * (1 - Z))) / (2 * sqrt(2 * N) * Z * (1 - Z)))        
        return P
    except Exception as e:
        print(f"An error occurred: {e}")
        return None