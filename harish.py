import speech_recognition as sr
import pyttsx3




listner=sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')

engine.setProperty('voice',voices[1].id)
engine.say("hello this is your virtual assistant . what can i do for you ")
engine.runAndWait()

try:
   with sr.Microphone() as source:

       print('listening  ')
       voice = listner.listen(source)
       command =listner.recognize_google(voice)
       command=command.lower()
       if 'hey' in command:

           print(command)



except:
    print('error')
    pass