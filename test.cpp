#include <iostream>
#include <cmath>
#include "portaudio.h"

#define SAMPLE_RATE (44100)
#define FRAMES_PER_BUFFER (64)
#define PI (3.14159265)

// This function generates a sine wave
int sine_callback(const void *inputBuffer, void *outputBuffer,
                  unsigned long framesPerBuffer,
                  const PaStreamCallbackTimeInfo *timeInfo,
                  PaStreamCallbackFlags statusFlags,
                  void *userData) {
    float *out = (float*)outputBuffer;
    unsigned int i;
    (void) inputBuffer; // Prevent unused variable warnings

    for(i = 0; i < framesPerBuffer; i++) {
        *out++ = static_cast<float>(0.2f * sin(2 * PI * 440 * i / SAMPLE_RATE));  // Left channel
        *out++ = static_cast<float>(0.2f * sin(2 * PI * 440 * i / SAMPLE_RATE));  // Right channel
    }

    return paContinue;
}

int main() {
    PaError err;
    PaStream *stream;
    PaStreamParameters outputParameters;

    err = Pa_Initialize();
    if (err != paNoError) {
        std::cerr << "PortAudio error: " << Pa_GetErrorText(err) << std::endl;
        return 1;
    }

    outputParameters.device = Pa_GetDefaultOutputDevice();
    if (outputParameters.device == paNoDevice) {
        std::cerr << "Error: No default output device" << std::endl;
        return 1;
    }

    outputParameters.channelCount = 2; // Stereo output
    outputParameters.sampleFormat = paFloat32; // 32-bit floating point output
    outputParameters.suggestedLatency = Pa_GetDeviceInfo(outputParameters.device)->defaultLowOutputLatency;
    outputParameters.hostApiSpecificStreamInfo = NULL;

    err = Pa_OpenStream(&stream, NULL, &outputParameters, SAMPLE_RATE, FRAMES_PER_BUFFER, paClipOff, sine_callback, NULL);
    if (err != paNoError) {
        std::cerr << "PortAudio error: " << Pa_GetErrorText(err) << std::endl;
        return 1;
    }

    err = Pa_StartStream(stream);
    if (err != paNoError) {
        std::cerr << "PortAudio error: " << Pa_GetErrorText(err) << std::endl;
        return 1;
    }

    std::cout << "Press Enter to quit..." << std::endl;
    std::cin.get();

    err = Pa_StopStream(stream);
    if (err != paNoError) {
        std::cerr << "PortAudio error: " << Pa_GetErrorText(err) << std::endl;
        return 1;
    }

    err = Pa_CloseStream(stream);
    if (err != paNoError) {
        std::cerr << "PortAudio error: " << Pa_GetErrorText(err) << std::endl;
        return 1;
    }

    Pa_Terminate();

    return 0;
}
