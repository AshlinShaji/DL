import pyttsx3
#class ===> init()
txt_sp=pyttsx3.init()

#convert to female voice
voices = txt_sp.getProperty('voices')
txt_sp.setProperty('voice', voices[1].id)
txt_sp.setProperty('volume', 0.1)

text=input("Enter the text:")
txt_sp.say(text)
txt_sp.runAndWait()

