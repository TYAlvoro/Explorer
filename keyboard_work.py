import serial
import pyttsx3


def make_message():
    speaker = pyttsx3.init()
    voices = speaker.getProperty("voices") 
    speaker.setProperty("voice", voices[2].id)
    speaker.setProperty("rate", 205) 
    text = ''
    while True:
        arduino = serial.Serial('COM3', 9600)
        letter = arduino.readline().decode('UTF-8')[0]
        if letter == 'B':
            text += ' '
            speaker.say('Пробел')
            speaker.runAndWait()
        elif letter == 'C':
            speaker.say('Стереть')
            speaker.runAndWait()
            text = text[:-1]
        elif letter == 'S':
            speaker.say('Отправить')
            speaker.runAndWait()
            return text.lower().capitalize()
        else:
            text += letter
            speaker.say(letter)
            speaker.runAndWait()
        arduino.close()