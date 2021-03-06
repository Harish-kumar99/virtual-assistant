import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listner=sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')

engine.setProperty('voice',voices[1].id)
def talk(text):

    engine.say(text)
    engine.runAndWait()
def take_command():
    try:
       with sr.Microphone() as source:

           print('listening  ')
           voice = listner.listen(source)
           command =listner.recognize_google(voice)
           command=command.lower()
           if 'hey' in command:
               command=command.replace('hey','')

               print(command)


    except:
        print('error')
        pass

    return command
def run_alexa():
    command=take_command()
    print(command)
    if 'play' in command :
        song=command.replace('play','')
        pywhatkit.playonyt(song)
        talk('ok i am playing'+song)
    elif 'time' in command:
        time=datetime.datetime.now().strftime('%I:%M %p')
        talk('current tine is'+time)
        print(time)
    elif 'who is' in command :
        person =command.replace('who is','')
        info=wikipedia.summary(person,2)
        print(info)
        talk(info)
    elif 'date ' in command:
        talk('sorry i have a headache')
    elif 'are you single' in command:
        talk('i am in relationship with wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('Please say the command again.')

while True:
    run_alexa()