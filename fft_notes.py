import numpy as np
import scipy.io.wavfile as wave
import matplotlib.pyplot as plt
from wave import Wave_read
from math import log2, pow
from scipy.signal import find_peaks_cwt as peaks
from scipy.optimize import leastsq
import numpy as np

A4 = 440
C0 = A4*pow(2, -4.75)
name = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
    
def pitch(freq):
    h = round(12*log2(freq/C0))
    octave = h // 12
    n = h % 12
    return name[n] + str(octave)

def Q():
	pass
def extract(filename):
    sample_rate, wav_file = wave.read(filename, 'r')
    N = len(wav_file)
    x = np.array(wav_file)
    w = np.fft.rfft(x)
    w = np.abs(w)
    w = [(x[0]) for x in w]
    spectrum = [i**2 for i in w]
    cutoff_idx = np.where(w < (np.max(w)/5)) [0]
    cutoff_idx = list(cutoff_idx)
    w2 = np.array(w.copy())
    w2[cutoff_idx] = 0

    # y2 = np.fft.irfft(w2)
    ax = plt.subplot(2,1,1)
    ax.set_title('Original melody')
    plt.plot(w)
    ax2 = plt.subplot(2,1,2)
    plt.plot(w2)
    ax2.set_title('Cleaned up')
    plt.show()
    freqs = np.fft.fftfreq(len(w2)) 

    ## use the Q learning here? to adjust the peak widths?
    fpeaks = peaks(w, np.arange(9000,24000,1000), noise_perc=0.1)
    id_freq = [freqs[x] for x in fpeaks]
    id_hz = [abs(x * sample_rate) for x in id_freq]
    notes = list(map(pitch, id_hz))
    print('Notes identified: ', notes)
    return notes


