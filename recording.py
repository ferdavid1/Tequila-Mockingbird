import speech_recognition as sr
import talkey
import speech_recognition as sr
import wave as wav
import os
from textblob import TextBlob
from google.cloud import speech

r = sr.Recognizer() 
speech_client = speech.Client()
tts = talkey.Talkey()

with sr.Microphone(3) as source:
    print("Tequila Mockingbird is listening!")
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)
    print('Audio obtained')
	try:
	    sample = speech_client.sample(audio, encoding=speech.Encoding.FLAC, sample_rate_hertz=44100)
		results = sample.recognize(language_code='en-US', max_alternatives=2)
		for result in results:
			for alternative in result.alternatives:
				print('=' * 20)
				print('transcript: ' + alternative.transcript)
				print('confidence: ' + str(alternative.confidence))
				if alternative.transcript == 'Tequila':
					print('Yo yo yo homie')
	except sr.UnknownValueError:
	    print("Sphinx could not understand audio")
	except sr.RequestError as e:
	    print("Google Could Speech error; {0}".format(e))

# with open('audio.txt', 'wb') as rec:
#     rec.write(r.recognize_sphinx(audio))
# if r.recognize_sphinx(audio) == 'tequila':
#     tts.say('What you need, fam?')


			os.chdir('text_out') # go back to parent directory, switch into text output directory
			with open(files.strip('.wav') + str(i) + '.txt', 'wb') as text: #initialize the file to which we will output the text
				