import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd

# Задаем частоту дискретизации
sampling_frequency = 10000  # 10 kHz

# Функция для генерации сигнала заданной частоты и длительности
def generate_signal(frequency, duration):
    t = np.arange(0, duration, 1/sampling_frequency)
    signal = np.sin(2 * np.pi * frequency * t)
    return signal

# Функция для воспроизведения звука
def play_sound(signal):
    sd.play(signal, sampling_frequency)
    sd.wait()

# Словарь с частотами для каждой цифры от 0 до 9
tones = {
    '1': (697, 1209),
    '2': (697, 1336),
    '3': (697, 1477),
    '4': (770, 1209),
    '5': (770, 1336),
    '6': (770, 1477),
    '7': (852, 1209),
    '8': (852, 1336),
    '9': (852, 1477),
    '0': (941, 1336)
}

# Ввод цифры от пользователя
digit = input("Введите цифру от 0 до 9: ")

# Проверка наличия цифры в словаре и воспроизведение соответствующего сигнала
if digit in tones:
    frequencies = tones[digit]
    duration = 0.5  # секунды
    signal = sum(generate_signal(f, duration) for f in frequencies)
    play_sound(signal)

    # Построение графика суммарного сигнала
    plt.plot(np.arange(0, duration, 1/sampling_frequency), signal)
    plt.xlabel('Time [s]')
    plt.ylabel('Amplitude')
    plt.title(f'Tone for digit {digit}')
    plt.grid(True)
    plt.show()
else:
    print("Неверная цифра. Введите число от 0 до 9.")
