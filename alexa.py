import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener =sr.Recognizer()
engine =pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)




def talk(text):
    engine.say(text)
    engine.runAndWait()
    
def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command=listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command=command.replace('alexa', '')
                print(command) 
    except:
        pass
    
    return command

def run_alexa():
    command=take_command()
    print(command)
    if 'play' in command:
        song=command.replace('play', '')
        talk('okay boss. trying to play your favorite song'+song)
        print('Searching for your Song, '+song)
        pywhatkit.playonyt(song)
        
    elif 'time' in command:
        time=datetime.datetime.now().strftime ('%I:%M %p')#('%H:%M')
        print(time)
        talk('Current time is ' + time)
        
    elif 'who is' in command:
        person = command.replace('who is', '')
        info= wikipedia.summary(person, 5)
        print(info)
        talk(info)
        
    elif 'joke' in command:
        talk(pyjokes.get_joke())
        
    else:talk('Say that command again, please. ')
        
while True:
    run_alexa()
    