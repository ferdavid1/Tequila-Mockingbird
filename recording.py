import speech_recognition as sr
#import talkey

r = sr.Recognizer()
tts = talkey.Talkey()
with sr.Microphone(3) as source:
    print("Tequila Mockingbird is listening!")
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)
    print('Audio obtained')
try:
    print("Sphinx thinks you said '" + r.recognize_sphinx(audio) + "'")
except sr.UnknownValueError:
    print("Sphinx could not understand audio")
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))

# with open('audio.txt', 'wb') as rec:
#     rec.write(r.recognize_sphinx(audio))
# if r.recognize_sphinx(audio) == 'tequila':
#     tts.say('What you need, fam?')

