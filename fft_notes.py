import numpy as np
import scipy.io.wavfile as wave
import matplotlib.pyplot as plt
from wave import Wave_read
from math import log2, pow
from scipy.signal import find_peaks_cwt as peaks

A4 = 440
C0 = A4*pow(2, -4.75)
name = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
    
def pitch(freq):
    h = round(12*log2(freq/C0))
    octave = h // 12
    n = h % 12
    return name[n] + str(octave)

def extract(filename):
    sample_rate, wav_file = wave.read(filename, 'r')
    sample_rate = sample_rate
    x = np.array(wav_file)
    w = np.fft.fft(x)
    w = np.abs(w)
    w = [(x[0]) for x in w]
    plt.plot(w)
    plt.show()
    freqs = np.fft.fftfreq(len(w)) 
    fpeaks = peaks(w, np.arange(9000,22000,1000))
    print(fpeaks)
    # idx = np.argmax(w)
    # print(idx)
    # freq = freqs[idx]
    # freq_in_hertz = abs(freq * sample_rate)
    # print(freq_in_hertz)
    # [26811, 27047, 84503, 111014, 154434]

extract('input_song.wav')

