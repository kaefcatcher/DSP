import numpy as np
import scipy.signal
import matplotlib.pyplot as plt
from numpy.fft import ifft,fft

def ex1():
    rect_pulse = np.repeat([0., 1., 0.], 100)

    conv_rect_rect = scipy.signal.convolve(rect_pulse, rect_pulse, mode='same')/100
    conv_tri_tri = scipy.signal.convolve(conv_rect_rect, conv_rect_rect, mode='same')/100
    conv_rect_tri = scipy.signal.convolve(rect_pulse, conv_rect_rect, mode='same')/100

    plt.figure(figsize=(15, 10))

    plt.subplot(3, 2, 1)
    plt.plot(rect_pulse)
    plt.title('Прямоугольный импульс')
    plt.ylim(-0.1, 1.1)

    plt.subplot(3, 2, 2)
    plt.plot(conv_rect_rect)
    plt.title('Свертка прямоугольных импульсов')
    plt.ylim(-0.1, 1.1)

    plt.subplot(3, 2, 3)
    plt.plot(conv_rect_rect)
    plt.title('Треугольный импульс')
    plt.ylim(-0.1, 1.1)

    plt.subplot(3, 2, 4)
    plt.plot(conv_tri_tri)
    plt.title('Свертка треугольных импульсов')
    plt.ylim(-0.1, 1.1)

    plt.subplot(3, 2, 5)
    plt.plot(rect_pulse)
    plt.plot(conv_rect_rect)
    plt.title('Прямоугольный и треугольный импульсы')
    plt.legend(['Прямоугольный', 'Треугольный'])
    plt.ylim(-0.1, 1.1)

    plt.subplot(3, 2, 6)
    plt.plot(conv_rect_tri)
    plt.title('Свертка прямоугольного и треугольного импульсов')

    plt.tight_layout()
    plt.show()

def create_signal(x):
    if x < 3:
        return 0
    elif x == 3:
        return 1
    else:
        return np.exp(-x)

def ex2():
    sig = []
    rect_pulse = np.repeat([0., 1., 0.], 100)
    for x in range(0, 300):
        sig.append(create_signal(x))
    conv_sig_rect = scipy.signal.convolve( sig,rect_pulse, mode='same') 
    plt.figure(figsize=(10, 10))

    plt.subplot(3, 1, 1)
    plt.plot(rect_pulse)
    plt.title('Прямоугольный импульс')

    plt.subplot(3, 1, 2)
    plt.plot(sig)
    plt.title('Экспоненциальный сигнал')

    plt.subplot(3, 1, 3)
    plt.plot(conv_sig_rect)
    plt.title('Свертка экспоненциального и прямоугольного импульсов')

    plt.tight_layout()
    plt.show()

def discrete_convolution(a, b):
    c = []
    len_a = len(a)
    len_b = len(b)
    for j in range(len_a + len_b - 1):
        sum_val = 0
        for i in range(max(0, j - len_b + 1), min(len_a, j + 1)):
            sum_val += a[i] * b[j - i]
        c.append(sum_val/100)
    return c



def ex3():
    plt.figure(figsize=(15, 10))
    rect_pulse = np.repeat([0., 1., 0.], 100)
    
    plt.subplot(3, 2, 1)
    plt.plot(rect_pulse)
    plt.title('Прямоугольный импульс')
    plt.ylim(-0.1, 1.1)
    
    sig = discrete_convolution(rect_pulse, rect_pulse)
    
    plt.subplot(3, 2, 2)
    plt.plot(sig)
    plt.title('Свертка прямоугольных импульсов')
    plt.ylim(-0.1, 1.1)
    
    plt.subplot(3, 2, 3)
    plt.plot(sig)
    plt.title('Треугольный импульс')
    plt.ylim(-0.1, 1.1)

    sig_tre = discrete_convolution(sig,sig)
    plt.subplot(3, 2, 4)
    plt.plot(sig_tre)
    plt.title('Свертка треугольных импульсов')
    plt.ylim(-0.1, 1.1)

    
    plt.subplot(3, 2, 5)
    plt.plot(rect_pulse)
    plt.plot(sig)
    plt.title('Прямоугольный и треугольный импульсы')
    plt.legend(['Прямоугольный', 'Треугольный'])
    plt.ylim(-0.1, 1.1)

    sig_rec_tre = discrete_convolution(rect_pulse,sig)
    plt.subplot(3, 2, 6)
    plt.plot(sig_rec_tre)
    plt.title('Свертка прямоугольного и треугольного импульсов')


    plt.show()


def circle_convolution(signal1, signal2):
    fft_signal1 = np.fft.fft(signal1)
    fft_signal2 = np.fft.fft(signal2)
    fft_result = fft_signal1 * fft_signal2
    return np.real(np.fft.ifft(fft_result))
    


def ex4():
    plt.figure(figsize=(15, 10))
    rect_pulse = np.repeat([0., 1., 0.], 100)
    
    plt.subplot(3, 2, 1)
    plt.plot(rect_pulse)
    plt.title('Прямоугольный импульс')
    plt.ylim(-0.1, 1.1)
    
    sig = circle_convolution(rect_pulse, rect_pulse)
    
    plt.subplot(3, 2, 2)
    plt.plot(sig)
    plt.title('Свертка прямоугольных импульсов')
    plt.ylim(-0.1, 1.1)
    
    plt.subplot(3, 2, 3)
    plt.plot(sig)
    plt.title('Треугольный импульс')
    plt.ylim(-0.1, 1.1)

    sig_tre = circle_convolution(sig,sig)
    plt.subplot(3, 2, 4)
    plt.plot(sig_tre)
    plt.title('Свертка треугольных импульсов')
    plt.ylim(-0.1, 1.1)

    
    plt.subplot(3, 2, 5)
    plt.plot(rect_pulse)
    plt.plot(sig)
    plt.title('Прямоугольный и треугольный импульсы')
    plt.legend(['Прямоугольный', 'Треугольный'])
    plt.ylim(-0.1, 1.1)

    sig_rec_tre = circle_convolution(rect_pulse,sig)
    plt.subplot(3, 2, 6)
    plt.plot(sig_rec_tre)
    plt.title('Свертка прямоугольного и треугольного импульсов')


    plt.show()

# ex4()

def ex5():
    duration = 0.03
    sample_rate = 10000
    eps = 0.00001
    freq_nums = [
        (941.0, 1336.0),
        (697.0, 1209.0),
    ]
    t = np.arange(0, duration, 1 / sample_rate)
    signal1 = np.sin(2.0 * np.pi * freq_nums[0][0] * t) + np.sin(2.0 * np.pi * freq_nums[0][1] * t)
    signal2 = np.sin(2.0 * np.pi * freq_nums[1][0] * t) + np.sin(2.0 * np.pi * freq_nums[1][1] * t)

    circle_conv_two_signal_math = np.array(
        [np.sum(signal1 * np.roll(signal2[::-1], i + 1)) for i in range(int(duration * sample_rate))])
    circle_conv_two_signal_fft = circle_convolution(signal1, signal2)


    plt.figure(figsize=(15, 8))

    plt.subplot(2, 3, 1)
    plt.plot(signal1)
    plt.title('Сигнал 1 (5 Гц)')

    plt.subplot(2, 3, 2)
    plt.plot(signal2)
    plt.title('Сигнал 2 (2 Гц)')

    plt.subplot(2, 3, 3)
    plt.plot(circle_conv_two_signal_math)
    plt.title('Циклическая свертка (своя)')

    plt.subplot(2, 3, 4)
    plt.plot(circle_conv_two_signal_fft)
    plt.title('Циклическая свертка (по теореме о свертке)')

    plt.tight_layout()
    plt.show()


    print(f'Длина циклической свертки (посчитана руками): {len(circle_conv_two_signal_math)}',f'Длина циклической свертки (посчитана по теореме): {len(circle_conv_two_signal_fft)}',f'Количества совпадений выражения fft(f * g) = fft(f) * fft(g): {np.count_nonzero((fft(circle_conv_two_signal_math) - (fft(signal1) * fft(signal2))) < eps)}',sep='\n')
# ex5()
    
ex1()
ex2()
ex3()
