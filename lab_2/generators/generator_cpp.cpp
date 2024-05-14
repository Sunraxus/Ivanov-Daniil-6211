#include <iostream>
#include <random>
#include <string>

using namespace std;

string GeneratorCPP() {
    random_device rd;
    mt19937 gen(rd());
    bernoulli_distribution dist(0.5);

    string BinarySequence;
    for (int i = 0; i < 128; ++i) {
        BinarySequence += (dist(gen) ? '1' : '0');
    }
    return BinarySequence;
}

int main() {
    string RandSequence = GeneratorCPP();
    cout << "A random binary sequence of 128 characters:\n" << RandSequence << endl;

    return 0;
}