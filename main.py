import speech_recognition as sr
import pyautogui
import time
from time import ctime
r = sr.Recognizer()

def record_audio(ask=False):
    with sr.Microphone() as source: # microphone as source
        if ask:
            print(ask)
        audio = r.listen(source)  # listen for the audio via source

        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)  # convert audio to text
        except sr.UnknownValueError: # error: recognizer does not understand
            print('I did not get that '+ctime())
        except sr.RequestError:
            print('Sorry, the service is down '+ctime()) # error: recognizer is not connected
        return voice_data

print("Please say something...")
while 1:
    voice_data = record_audio()
    if 'exit' in voice_data:
        print('exit in '+ctime())
        exit()
    pyautogui.typewrite(voice_data)
    pyautogui.press('Enter')