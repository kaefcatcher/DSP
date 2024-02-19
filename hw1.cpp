#include <iostream>
#include <vector>
#include <cmath>
#include <chrono>
#include <thread>
#include <portaudio.h>

const double A = 1.0; // Amplitude of signals
const int fs = 44100; // Sampling frequency
const double duration = 10.0; // Duration of sound

// Frequencies of dual-channel signals
std::vector<std::array<double, 2>> freq_nums = {
    {941.0, 1336.0},
    {697.0, 1209.0},
    {697.0, 1336.0},
    {697.0, 1477.0},
    {770.0, 1209.0},
    {770.0, 1336.0},
    {770.0, 1477.0},
    {852.0, 1209.0},
    {852.0, 1336.0},
    {852.0, 1477.0}
};

std::vector<double> get_signal(double t, std::array<double, 2> freq) {
    std::vector<double> signal;
    signal.reserve(fs * duration);
    for (double i = 0; i < t; i += 1.0 / fs) {
        signal.push_back(A * std::sin(2.0 * M_PI * freq[0] * i) + A * std::sin(2.0 * M_PI * freq[1] * i));
    }
    return signal;
}

int playCallback(const void *inputBuffer, void *outputBuffer,
                  unsigned long framesPerBuffer,
                  const PaStreamCallbackTimeInfo *timeInfo,
                  PaStreamCallbackFlags statusFlags,
                  void *userData) {
    float *out = (float*)outputBuffer;
    std::vector<double> *signal = (std::vector<double>*)userData;

    for (unsigned long i = 0; i < framesPerBuffer; i++) {
        for (size_t j = 0; j < signal->size(); j++) {
            *out++ = (*signal)[j]; // Assuming signal is mono
        }
    }

    return paContinue;
}

void play_signal(const std::vector<double>& signal) {
    Pa_Initialize();

    PaStream *stream;
    Pa_OpenDefaultStream(&stream, 0, 2, paFloat32, fs, paFramesPerBufferUnspecified, playCallback, (void*)&signal);
    Pa_StartStream(stream);

    std::this_thread::sleep_for(std::chrono::milliseconds(static_cast<int>(duration * 1000)));

    Pa_StopStream(stream);
    Pa_CloseStream(stream);
    Pa_Terminate();
}

int main() {
    char command;
    std::vector<double> t;
    t.reserve(fs * duration);
    for (double i = 0; i < duration; i += 1.0 / fs) {
        t.push_back(i);
    }

    std::cout << "Enter command (0-9 to play a tone, 'array' to play a sequence, 'exit' to quit): ";
    while (std::cin >> command && command != 'exit') {
        if (command >= '0' && command <= '9') {
            int num = command - '0';
            play_signal(get_signal(duration, freq_nums[num]));
        } else if (command == 'a') {
            std::vector<int> nums;
            int num;
            while (std::cin >> num) {
                nums.push_back(num);
            }
            for (int num : nums) {
                if (num >= 0 && num < freq_nums.size()) {
                    play_signal(get_signal(duration, freq_nums[num]));
                } else {
                    std::cout << "Invalid frequency number: " << num << std::endl;
                }
            }
        } else {
            std::cout << "Enter correct command" << std::endl;
        }
        std::cout << "Enter command (0-9 to play a tone, 'array' to play a sequence, 'exit' to quit): ";
    }
    return 0;
}
