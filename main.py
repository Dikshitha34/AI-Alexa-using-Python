import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


# engine.say('I am your alexa')
# engine.say('What are you doing?')
# engine.runAndWait()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('Listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)


    except:
        pass
    return command


def run_alexa():
    command = take_command()
    if 'play' in command:
        song=command.replace('play','')
        talk('Playing'+song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time=datetime.datetime.now().strftime('%H:%M %p')
        # print(time)
        talk('Current time is '+time)

    elif 'who is ' in command:
        person=command.replace('who is','')
        info=wikipedia.summary(person,2)
        print(info)
        talk(info)

    elif 'date' in command:
        talk('Sorry, I am just an AI-based voice assistant for you. If you have any questions or need assistance with anything, feel free to ask, and I will do my best to help! ')

    elif 'joke' in command:
        print(pyjokes.get_joke())
        talk(pyjokes.get_joke())
    else:
        talk('Please say the command again...')


while True:
    run_alexa()

