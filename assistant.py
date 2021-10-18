import os
import random
import datetime
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import smtplib

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

def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login('myemailID@gmail.com', "myPassword")
    server.sendmail("myemailID@gmail.com", to, content)
    server.close()


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

        elif 'code' in query:
            codePath = "C:\\Users\\asus\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
            speak("Opening Visual Studio Code")

        elif 'email to' in query:
            try:
                speak("What is the message to be sent!")
                content = takeCommand()
                to = "xyz@gmail.com"
                sendEmail(to, content)
                speak("Email had been sent to ", to)

            except Exception as e:
                print(e)
                speak("Sorry! Unable to send the Email...")