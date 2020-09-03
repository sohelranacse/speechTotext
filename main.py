import speech_recognition as sr
import pyautogui
import time

def my_voice():
    r = sr.Recognizer()
    with sr.Microphone() as source: # microphone as source
        audio = r.listen(source)  # listen for the audio via source
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)  # convert audio to text
        except sr.UnknownValueError: # error: recognizer does not understand
            print('I did not get that.')
        except sr.RequestError: # error: recognizer is not connected
            print('Sorry, this service is down.')
        return voice_data

while 1:
    say = pyautogui.confirm('Say something...')
    if say == 'OK':
        voice_data = my_voice()
        pyautogui.write(voice_data)
        pyautogui.press('Enter')
        time.sleep(2)
    else:
        exit()