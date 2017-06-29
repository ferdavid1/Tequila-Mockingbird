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
    x = np.array(wav_file)
    w = np.fft.fft(x)
    w = np.abs(w)
    w = [(x[0]) for x in w]
    plt.plot(w)
    plt.show()
    freqs = np.fft.fftfreq(len(w)) 

    ### use the Q learning here? to adjust the peak widths?
    fpeaks = peaks(w, np.arange(9000,24000,1000))
    id_freq = [freqs[x] for x in fpeaks]
    id_hz = [abs(x * sample_rate) for x in id_freq]
    # freq_in_hertz = 
    # print(freq_in_hertz)
    # [26865, 83991, 101873, 111138, 141505, 154264]
    notes = list(map(pitch, id_hz))
    print(notes)

extract('input_song.wav')

