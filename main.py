
import pyttsx3
import datetime
import speech_recognition as sr
import os
import wikipedia
import PyPDF2
import smtplib
import pyaudio
import subprocess
import webbrowser
import pynput.keyboard
from pynput.keyboard import Key, Controller


keyboard = Controller()
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)
keyboard = pynput.keyboard.Controller()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if 1 <= hour <= 4:
        speak('that is not good boss ,you should sleep now!')
    elif 6 <= hour <= 12:
        speak('good morning sir!')
    elif 12 <= hour <= 18:
        speak('good afternoon sir !')
    else:
        speak('good evening sir!')
    speak('Hi boss;i am friday;how can I help you?')


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('listening....')
        r.pause_threshold = 0.5
        r.energy_threshold = 100

        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')  # Using google for voice recognition.
        print(f"User said: {query}\n")
    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query


if __name__ == "__main__":
    wishme()

    query = takeCommand().lower()
    # Logic for executing tasks based on query
    if 'who is' in query:
        speak('Searching Wikipedia...')
        query = query.replace("who is", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        print(results)
        speak(results)

    elif 'what is' in query:
        speak('Searching Wikipedia...')
        query = query.replace("what is", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        print(results)
        speak(results)
    elif 'tell me about' in query:
        speak('Searching Wikipedia...')
        query = query.replace("tell me about", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        print(results)

        speak(results)

    elif 'sleep' in query or 'shutdown' in query:
        speak('good bye boss;have a good day!')
        exit()
    elif 'i want to open pdf file' in query:
        speak('okk boss, please tell which file you want to open')
    elif 'open the pdf file hazards' in query:
        speak('here you go boss')
        query = query.replace("open the pdf file", "")
        os.startfile("pipelining hazards.pdf")
    elif 'the time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Sir, the time is {strTime}")
    elif 'open spotify' in query:
        speak('here you go boss')
        webbrowser.open("https://open.spotify.com/track/5aXsYlFhJIOHCvxnna7jdP?si=c934bf65da224181")
    elif 'stop it' in query:
        keyboard.press(Key.media_play_pause)
        keyboard.release(Key.media_play_pause)
    elif 'play' in query:
        keyboard.press(Key.media_play_pause)
        keyboard.release(Key.media_play_pause)
    elif 'next' in query:
        keyboard.press(Key.media_next)
        keyboard.release(Key.media_next)
    elif 'previous' in query:
        keyboard.press(Key.media_previous)
        keyboard.release(Key.media_previous)
        keyboard.press(Key.media_previous)
        keyboard.release(Key.media_previous)
    elif 'volume up' in query:
        keyboard.press(Key.media_volume_up)
        keyboard.release(Key.media_volume_up)
    elif 'volume down' in query:
        keyboard.press(Key.media_volume_down)
        keyboard.release(Key.media_volume_down)
    elif 'scroll up' in query:
        keyboard.press(Key.scroll_lock)
        keyboard.press(Key.up)
        keyboard.release(Key.up)
        keyboard.release(Key.scroll_lock)
        keyboard.press(Key.scroll_lock)
        keyboard.press(Key.up)
        keyboard.release(Key.up)
        keyboard.release(Key.scroll_lock)
        keyboard.press(Key.scroll_lock)
        keyboard.press(Key.up)
        keyboard.release(Key.up)
        keyboard.release(Key.scroll_lock)
    elif 'scroll down' in query:
        keyboard.press(Key.scroll_lock)
        keyboard.press(Key.down)
        keyboard.release(Key.up)
        keyboard.release(Key.scroll_lock)
        keyboard.press(Key.scroll_lock)
        keyboard.press(Key.up)
        keyboard.release(Key.up)
        keyboard.release(Key.scroll_lock)
        keyboard.press(Key.scroll_lock)
        keyboard.press(Key.up)
        keyboard.release(Key.up)
        keyboard.release(Key.scroll_lock)
    elif 'select text' in query:
        keyboard.press(Key.ctrl)
        keyboard.press('w')
        keyboard.release('w')
        keyboard.release(Key.ctrl)
        keyboard.press(Key.ctrl)
        keyboard.press('w')
        keyboard.release('w')
        keyboard.release(Key.ctrl)
        keyboard.press(Key.ctrl)
        keyboard.press('w')
        keyboard.release('w')
        keyboard.release(Key.ctrl)
        keyboard.press(Key.ctrl)
        keyboard.press('w')
        keyboard.release('w')
        keyboard.release(Key.ctrl)
    elif 'close window' in query:
        keyboard.press(Key.ctrl)
        keyboard.press('w')
        keyboard.release('w')
        keyboard.release(Key.ctrl)
        keyboard.press(Key.ctrl)
    elif 'window' in query:
        keyboard.press(Key.cmd)
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)
        keyboard.release(Key.cmd)
    elif 'go' in query or 'enter' in query:
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
    elif 'left' in query:
        keyboard.press(Key.left)
        keyboard.release(Key.left)

    elif 'right side' in query:
        keyboard.press(Key.right)
        keyboard.release(Key.right)
    elif 'upper' in query:
        keyboard.press(Key.up)
        keyboard.release(Key.up)
    elif 'down' in query:
        keyboard.press(Key.down)
        keyboard.release(Key.down)
    elif 'control' in query:
        keyboard.press(Key.ctrl)
        keyboard.release(Key.ctrl)
    elif 'open map' in query:
        webbrowser.open('https://www.google.co.in/maps/@23.2801191,88.4189253,14z')
        speak('what location do you want to search in?')
        cm = takeCommand().lower()
        webbrowser.open(f"{cm}")
    elif 'text dad' in query:
        speak('tell what you want to send')
        cm = takeCommand().lower()
        pywhatkit.sendwhatmsg_instantly("+919735134404", f"{cm}", 6, 25)
    elif 'text mom' in query or 'text mum' in query:
        speak('tell what you want to send')
        cm = takeCommand().lower()
        pywhatkit.sendwhatmsg_instantly("+919434953902", f"{cm}", 6, 25)
    elif 'open youtube song' in query:
        speak('tell what song you want to open')
        cm = takeCommand().lower()
        pywhatkit.playonyt(f"{cm}")
