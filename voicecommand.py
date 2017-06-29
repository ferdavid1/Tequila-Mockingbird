import speech_recognition as sr 
import pyaudio
import subprocess
import wave
import os
import time
 
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 32000
CHUNK = 2048
RECORD_SECONDS = 3
WAVE_OUTPUT_FILENAME = "sound_file.wav"
 
audio = pyaudio.PyAudio()
 
# start Recording
stream = audio.open(format=FORMAT, channels=CHANNELS,
                rate=RATE, input=True,
                frames_per_buffer=CHUNK, )
print ("recording command...")
frames = []
 
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)
print ("finished recording")
 
 
# stop Recording
stream.stop_stream()
stream.close()
audio.terminate()
 
waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
waveFile.setnchannels(CHANNELS)
waveFile.setsampwidth(audio.get_sample_size(FORMAT))
waveFile.setframerate(RATE)
waveFile.writeframes(b''.join(frames))
waveFile.close()
r = sr.Recognizer()
with sr.AudioFile('sound_file.wav') as source:
    audio = r.record(source) 
    r.adjust_for_ambient_noise(source)
    with open(r"cred.json", "r") as f:  
        credentials_json = f.read()
        try:
            answer = r.recognize_google_cloud(audio, credentials_json=credentials_json, language='en-US')
        except sr.UnknownValueError:
            print("Google Cloud Speech could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Cloud Speech service; {0}".format(e))
        print(answer)
        if answer == 'bird ': # change to tequila for demo
            exec(open('client.py').read())
            time.sleep(10)
            S_RECORD_SECONDS = 5
            S_WAVE_OUTPUT_FILENAME = "input_song.wav"
             
            s_audio = pyaudio.PyAudio()
            print('\nPrepare to sing your melody!\n')
            time.sleep(5)
            # start Recording
            s_stream = s_audio.open(format=FORMAT, channels=CHANNELS,
                            rate=RATE, input=True,
                            frames_per_buffer=CHUNK, )
            print ("recording song...")
            s_frames = []
             
            for i in range(0, int(RATE / CHUNK * S_RECORD_SECONDS)):
                s_data = s_stream.read(CHUNK)
                s_frames.append(s_data)
            print ("finished recording")

                            # stop Recording
            s_stream.stop_stream()
            s_stream.close()
            s_audio.terminate()
             
            s_waveFile = wave.open(S_WAVE_OUTPUT_FILENAME, 'wb')
            s_waveFile.setnchannels(CHANNELS)
            s_waveFile.setsampwidth(s_audio.get_sample_size(FORMAT))
            s_waveFile.setframerate(RATE)
            s_waveFile.writeframes(b''.join(s_frames))
            s_waveFile.close()