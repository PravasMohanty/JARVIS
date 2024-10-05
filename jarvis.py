import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import subprocess
import random

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
print(voices)   # Check number of voice available


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")


def takeCommand():
    """Takes aurdio input and return string output"""

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}\n")
        except Exception as e:
            # print(e)
            print("Sorry I couldn't understand Please say again..")
            return "None"
        return query


def open_whatsapp():
    try:
        subprocess.Popen("start whatsapp://", shell=True)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    wish()
    speak(
        "I am Jarvis . your personal virtual assistant and I will aid you in every way I can"
    )
    while True:
        query = takeCommand().lower()
        if "wikipedia" in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        if "exit" in query:
            speak("Exiting Jarvis dot A.I.")
            break
        elif "open youtube" in query:
            speak("Opening. Youtube.")
            webbrowser.open("https://www.youtube.com")

        elif "open google" in query:
            speak("Opening. Google.")
            webbrowser.open("https://www.google.com")

        elif "song" in query:
            music_dir = "C:\\Users\\prava\\Music\\Music"
            songs = os.listdir(music_dir)
            print(songs)
            s = random.randrange(1, 3)
            os.startfile(os.path.join(music_dir, songs[s - 1]))

        elif "time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        elif "program" in query:
            speak("Opening ")
            f_dir = "C:\\Users\\prava\\Documents\\Programming"
            os.startfile(f_dir)

        elif "download" in query:
            speak("Opening Downloads folder")
            f_dir = "C:\\Users\\prava\\Downloads"
            os.startfile(f_dir)

        elif "whatsapp" in query:
            speak("Opening Whatsapp...")
            open_whatsapp()

        elif "code" in query:
            speak("Opening Microsoft VS Code...")
            codepath = (
                "C:\\Users\\prava\\AppData\\Local\\Programs\\Microsoft VS Code\\Code"
            )
            os.startfile(codepath)

        elif "mail" in query:
            speak("Opening Your Gmail.")
            webbrowser.open("https://mail.google.com/mail/u/0/?ogbl#inbox")

        elif "music" in query:
            speak("Please speak the name of song you want to hear")
            q3 = takeCommand().lower()
            q3 = q3.replace("play", "")
            web = "https://open.spotify.com/search/" + q3
            webbrowser.open(web)
