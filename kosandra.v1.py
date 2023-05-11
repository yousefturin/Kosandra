import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia as wk
import pyjokes as jk
from tkinter import *
from pygame import mixer

root = Tk()
root.title('Kosandra')
root.iconbitmap('C:/Users/ENVY/Downloads/mic2.ico')
root.geometry("500x500")

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
newVoiceRate = 168
engine.setProperty('rate', newVoiceRate)
engine.setProperty('voice', voices[1].id)


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
            if 'hey ' in command:
                command = command.replace('hey ', '')
                engine.say('yes yousef')
                engine.say('How I can Help you')
                engine.runAndWait()
                voice = listener.listen(source)
                command = listener.recognize_google(voice)
                command = command.lower()
                print(command)

    except:
        pass
    return command


def listen_again():
    with sr.Microphone() as source:
        print('Listening...2')
        engine.runAndWait()
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        command = command.lower()
    return command


def run_kosandra():
    engine.runAndWait()
    command = take_command()
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('It is ' + time)

    elif 'go on a date' in command:
        talk('Sorry, you are so ugly i will never go on a date with you')
        talk('ops, i was just kidding i would love to but i can')
    elif 'how about to  go on a date with me' in command:
        talk('Sorry, you are so ugly i will never go on a date with you')
        talk('ops, i was just kidding i would love to but i can')
    elif 'would you like to go on a date with me' in command:
        talk('Sorry, you are so ugly i will never go on a date with you')
        talk('ops, i was just kidding i would love to but i can')

    elif 'who are you' in command:
        talk('i am a machine that was created by the engineer named'
             ' yousef rayyan in 2021 and my purpose is to serve you')

    elif 'are you in relationship' in command:
        talk('I am in relationship with your voice')
    elif 'are you single' in command:
        talk('No, I am NOT single ')

    elif 'what is' in command:
        search = command.replace('what is', '')
        info = wk.summary(search, 1)
        print(info)
        talk(info)

    elif 'who is' in command:
        search1 = command.replace('who is', '')
        info = wk.summary(search1, 1)
        print(info)
        talk(info)

    elif 'how to' in command:
        search2 = command.replace('how to', '')
        info = wk.summary(search2, 1)
        print(info)
        talk(info)

    elif ' tell me a joke' in command:
        talk(jk.get_joke())
    elif'Do you love me' in command:
        talk('You seems so lonely   should i call someone?')
    elif 'spell' in command:
        spell = command.replace('spell', '')
        newVoiceRate = 20
        engine.setProperty('rate', newVoiceRate)
        talk(spell)
    elif 'fart for me' in command:
        volume = engine.getProperty('volume')
        engine.setProperty('volume', volume - 0.25)
        talk('come closer')
        talk('are you ready')
        mixer.init()
        mixer.music.load("c:/Users/ENVY/Downloads/fartSound.mp3")
        # mixer.music.set_volume(0.7)
        mixer.music.play()
        engine.runAndWait()
        listen_again()

    elif 'turbo' in command:
        talk('shototo shottotoo')

    else:
        engine.runAndWait()
        talk('Sorry what is it again.')
        engine.save_to_file(command, command+'.mp3')
        engine.runAndWait()
        run_kosandra()


mic_btn = PhotoImage(file='C:/Users/ENVY/AppData/Roaming/JetBrains/PyCharmCE2020.1/scratches/mic.png')
img_label = Label(image=mic_btn, background="black")
Label(text="KOSANDRA", font=("", 10, "bold"), fg="black", border=0).pack(pady=30)
Label(text="listing", font=("", 10, "bold"), fg="black", border=0).pack(pady=1)

mic = Button(root, image=mic_btn, command=run_kosandra, borderwid=0)
mic.pack(pady=100)

if __name__ == '__main__':
    mainloop()
