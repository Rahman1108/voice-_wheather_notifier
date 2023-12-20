import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime 
import pyjokes
def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("recognizing...")
            data = recognizer.recognize_google(audio)
            print(data)
        except sr.UnknownValueError:
            print(" Not Understand ")
def speechtx(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate',130)
    engine.say(x)
    engine.runAndWait()
if __name__ == "__main__":

    if "Hey chintu" in sptext().lower() :
        speechtx("AT your service please command....")
    else:
        speechtx("wrong coded your are not my owner....")
