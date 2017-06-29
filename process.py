# AUDIO TO MIDI ALGORITHM - https://github.com/justinsalamon/audio_to_midi_melodia
# BPM DETECTION - https://github.com/scaperot/the-BPM-detector-python/blob/master/bpm_detection/bpm_detection.py
import os
from bpm import final
def get_bpm(file):
	return final(file)
def get_midi(infile, outfile, bpm):
	bpm = get_bpm(infile)
	os.system('python audio_to_midi_melodia.py '+infile+' '+outfile+' '+int(bpm)+' --smooth 0.25 --minduration 0.05 --jams')
