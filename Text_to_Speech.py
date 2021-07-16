import pyttsx3
engine=pyttsx3.init()
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
while True:
    speech = input('Type to speak: ')
    speak(speech)
    