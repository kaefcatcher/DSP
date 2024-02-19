#include <iostream>
#include <vector>
#include <cmath>
#include <thread>
#include <chrono>

constexpr double samplingFrequency = 10000.0; // Частота дискретизации в Гц
constexpr double samplingPeriod = 1.0 / samplingFrequency; // Период дискретизации в секундах

// Функция для генерации сигнала с заданной частотой
std::vector<double> generateSignal(double frequency, double duration) {
    std::vector<double> signal;
    int numSamples = duration * samplingFrequency;
    for (int i = 0; i < numSamples; ++i) {
        double sample = sin(2.0 * M_PI * frequency * i * samplingPeriod);
        signal.push_back(sample);
    }
    return signal;
}

// Функция для воспроизведения сигнала
void playSignal(const std::vector<double>& signal) {
    for (double sample : signal) {
        std::cout << sample << std::endl; // Здесь будет ваша логика воспроизведения звука
        std::this_thread::sleep_for(std::chrono::microseconds(static_cast<int>(1000000 * samplingPeriod))); // Ожидание до следующего семпла
    }
}

// Функция для воспроизведения цифры
void playDigit(int digit) {
    if (digit < 0 || digit > 9) {
        std::cerr << "Недопустимая цифра" << std::endl;
        return;
    }

    // Получение частот из таблицы
    constexpr double frequencies[4][3] = {
        {697.0, 770.0, 852.0}, // для 1, 2, 3
        {941.0, 1336.0, 1477.0}, // для 4, 5, 6
        {1209.0, 1336.0, 1477.0}, // для 7, 8, 9
        {941.0, 1209.0, 1633.0} // для *, 0, #
    };

    std::vector<double> signal;
    for (int i = 0; i < 3; ++i) {
        signal = generateSignal(frequencies[digit / 3][i], 0.5);
        playSignal(signal);
    }
}

int main() {
    char choice;
    do {
        std::cout << "Введите цифру от 0 до 9: ";
        int digit;
        std::cin >> digit;

        playDigit(digit);

        std::cout << "Хотите ввести еще одну цифру? (y/n): ";
        std::cin >> choice;
    } while (choice == 'y' || choice == 'Y');

    return 0;
}
