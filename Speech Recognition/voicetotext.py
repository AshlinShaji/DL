#class
#Recognizer:
import speech_recognition as sr
def speech_txt():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please say something:")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("You said: " + text)
    except :
        print("Sorry, I could not understand the audio.")

speech_txt()