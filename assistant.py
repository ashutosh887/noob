import pyttsx3
import speech_recognition as sr
import wikipedia
import random
import os
import webbrowser
import datetime

engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


# Speak Function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# Greet Function
def greet():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>12 and hour<6:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Noob. Please tell me how may I help you.")


def takeCommand():
    # It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio= r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print("User said : ", query)

    except Exception as e:
        # print(e)
        print("Say that again Please")
        return "None"
    return query

if __name__ == "__main__":
    greet()

    while True:
        query = takeCommand().lower()

    # Logics to execute our Commands
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to WikiPedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")
        
        elif 'open instagram' in query:
            webbrowser.open("instagram.com")

        elif 'play music' in query:
            songsFolder = "A:\\Songs"
            songs = os.listdir(songsFolder)
            print(songs)
            os.startfile(os.path.join(songsFolder, songs[0]))

        elif 'the time' in query:
            time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir the Time is {time}")