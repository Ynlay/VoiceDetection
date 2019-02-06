import os
import speech_recognition as sr
# import CameraFaceDetection as cd
from time import sleep 
from gtts import gTTS

# Obtain audio from microphone
r = sr.Recognizer()
mic = sr.Microphone()

# Listens 
def listenSource(): 
    with mic as source:
        print("Say Something!") 
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        audio = r.recognize_google(audio, language="en-US")
        #audio = r.recognize_google(audio, language="el-GR")
        return audio


# Speaks
def speak(textToSpeech):
    print("Clearing throat...")
    tts = gTTS(textToSpeech, lang='en')  # gTTS requires internet connection...
    tts.save("textToSpeech.mp3")    
    os.startfile("textToSpeech.mp3")  # Need to improve on that. maybe mpg321!

# Will be adding all the different functionalities here
def functionalities(voiceInput):
    print(voiceInput)
    print("casefold: " + voiceInput.casefold())

    if (voiceInput == "Hello".casefold()):
        speak("Greetings!")
        print("Greetings!")


# Recognize speech using Google Speech Recognition
try:
    # For testing purposes, we're just using the default API key
    # to use another API key, use 
    # 'r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")
    # instead of 'r.recognize_google(audio)'
    while(True):
        voiceInput = listenSource()
        print("Google Speech Recognition thinks you said: " + voiceInput)
        speak("You Said: " + voiceInput)
        
        # Exit the loop if the command was exit 
        if ("exit" in voiceInput): 
            print("Exiting...")
            speak("Thanks for your cooperation human, I am shutting down now...")
            break

        # Execute functionalities
        functionalities(voiceInput)

except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google; {0}".format(e))
