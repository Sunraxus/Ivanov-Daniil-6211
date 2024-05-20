from math import sqrt
from scipy.special import erfc
from mpmath import gammainc

from constants import SEQUENCE_CPP, SEQUENCE_JAVA, BLOCK_SIZE, PI_VALUES


def read_txt(path: str) -> str:
    try:
        with open(path, 'r') as file:
            text = file.read()
        return text
    except FileNotFoundError:
        print(f"Error: File '{path}' not found.")
        return None
    except Exception as e:
        print(f"Unexpected error occurred while reading file '{path}': {e}.")
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
    

def longest_sequence_test(sequence: str) -> float:
    try:
        N = len(sequence)
        block_max_lengths = {i: 0 for i in range(0, BLOCK_SIZE)}
        for step in range(0, N, BLOCK_SIZE):
            block = sequence[step:step + BLOCK_SIZE]
            current_length = 0
            max_length = 0
            for bit in block:
                if bit == "1":
                    current_length += 1
                else:
                    current_length = 0
                max_length = max(max_length, current_length)
            block_max_lengths[max_length] = block_max_lengths.get(max_length, 0) + 1
        v = {i: 0 for i in range(1, 5)}
        for i in block_max_lengths:
            match i:
                case 0 | 1:
                    v[1] += block_max_lengths[i]
                case 2:
                    v[2] += block_max_lengths[i]
                case 3:
                    v[3] += block_max_lengths[i]
                case _:
                    v[4] += block_max_lengths[i]
        for i in range(4):
            xi_square = (pow((v[i+1] - 16 * PI_VALUES[i]), 2) / (16 * PI_VALUES[i]))
        P = gammainc(3 / 2, xi_square / 2)
        return P    
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    
    
def main():
    sequence_cpp = read_txt(SEQUENCE_CPP)
    sequence_java = read_txt(SEQUENCE_JAVA)
    
    print("Результаты тестов для последовательности C++:")
    freq_test_cpp = frequency_bitwise_test(sequence_cpp)
    consec_bits_test_cpp = consecutive_bits_test(sequence_cpp)
    longest_seq_test_cpp = longest_sequence_test(sequence_cpp)
    print(f"Тест на частоту битов: {freq_test_cpp}")
    print(f"Тест на последовательные биты: {consec_bits_test_cpp}")
    print(f"Тест на самую длинную последовательность: {longest_seq_test_cpp}")
    
    print("\nРезультаты тестов для последовательности Java:")
    freq_test_java = frequency_bitwise_test(sequence_java)
    consec_bits_test_java = consecutive_bits_test(sequence_java)
    longest_seq_test_java = longest_sequence_test(sequence_java)
    print(f"Тест на частоту битов: {freq_test_java}")
    print(f"Тест на последовательные биты: {consec_bits_test_java}")
    print(f"Тест на самую длинную последовательность: {longest_seq_test_java}")


if __name__ == "__main__":
    main()