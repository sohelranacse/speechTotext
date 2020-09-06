import speech_recognition as sr
import pyautogui
import sys

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

confirm = pyautogui.confirm(title='Facebook Auto Messaging', text='Welcome to my application', buttons=['Start', 'Close'])
while 1:
    if confirm == 'Start' or confirm == 'Start Again':
        voice_data = my_voice()
        if voice_data == 'Close' or voice_data == 'close':
            confirm = pyautogui.confirm(title='Facebook Auto Messaging', text='Are you sure you want to close it?', buttons=['OK', 'Start Again'])
        elif voice_data !='':
            print(voice_data)
            pyautogui.write(voice_data)
            pyautogui.press('Enter')
    else:
        sys.exit()