import speech_recognition as sr
import pyttsx3
import wikipedia

def speak(string):
    eng = pyttsx3.init()
    eng.say(string)
    eng.runAndWait()
    
def userInput():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        query = r.recognize_google(audio)
    return query

def out():
    query = userInput().lower()
    result = wikipedia.summary(query, sentences=3)
    print(result)
    speak("According to wikipediaa")
    speak(result)
    
speak("Hey there nitro here ask me anything")
out()
