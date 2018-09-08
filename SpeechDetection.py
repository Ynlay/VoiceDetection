import os
import speech_recognition as sr
import CameraFaceDetection as cd
import ModernArt as ma
from time import sleep 
from docx import Document
from gtts import gTTS
from mutagen.mp3 import MP3

# Obtain audio from microphone
r = sr.Recognizer()


# Listens 
def listenSource():
    print("Say Something!")
    with sr.Microphone() as source:
        audio = r.listen(source)
    print("Got it!")
    return audio


# Speaks
def speak(textToSpeech):
    print("Clearing throat...")
    tts = gTTS(textToSpeech, lang='en')  # gTTS requires internet connection...
    tts.save("textToSpeech.mp3")    
    os.startfile("textToSpeech.mp3")  # Need to improve on that. maybe mpg321!
    mp3Length = MP3("textToSpeech.mp3").info.length
    sleep(mp3Length)  # In order to avoid listening to itself.


# Will be adding all the different functionalities here
def functionalities(voiceInput):
    print(voiceInput)
    print("casefold: " + voiceInput.casefold())
    if (voiceInput == "Hello Athena".casefold()):
        speak("Greetings!")
        print("Greetings!")

    if (voiceInput == "Face Detection".casefold()):
        cd.CameraDetection("haarcascade_frontalface_default.xml")

    if ("Draw".casefold() in voiceInput.casefold()):
        ma.Draw()


# Recognize speech using Google Speech Recognition
try:
    # For testing purposes, we're just using the default API key
    # to use another API key, use 
    # 'r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")
    # instead of 'r.recognize_google(audio)'
    while(True):
        voiceInput = r.recognize_google(listenSource())
        print("Google Speech Recognition thinks you said: " + voiceInput)
        speak("I think you just said: " + voiceInput)
        
        # Exit the loop if the command was exit 
        if ("exit" in voiceInput): 
            print("Exiting...")
            break

        # Execute functionalities
        functionalities(voiceInput)

except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google; {0}".format(e))