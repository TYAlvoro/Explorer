import serial
import pyttsx3
from random import sample


def studying():
    speaker = pyttsx3.init()
    voices = speaker.getProperty("voices") 
    speaker.setProperty("voice", voices[2].id)
    speaker.setProperty("rate", 205) 
    speaker.say('Нажимайте кнопки. Я буду озвучивать каждое нажатие. Старайтесь запоминать шифр. Удачи')
    speaker.runAndWait()
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
            break
        else:
            text += letter
            speaker.say(letter)
            speaker.runAndWait()
        arduino.close()


def check_knowledge():
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщьыъэюя1234567890.,'.upper()
    speaker = pyttsx3.init()
    voices = speaker.getProperty("voices") 
    speaker.setProperty("voice", voices[2].id)
    speaker.setProperty("rate", 205) 
    speaker.say('Итак. Давайте проверим ваши знания. Я произнесу названия десяти символов, которые вы должны нажать. Вперед!')
    speaker.runAndWait()
    errors = list()
    letters = sample(alphabet, 10)
    for m in letters:
        speaker.say(m)
        speaker.runAndWait()
        arduino = serial.Serial('COM3', 9600)
        letter = arduino.readline().decode('UTF-8')[0]
        if letter == 'S':
            return
        if m == letter:
            speaker.say('Правильно')
            speaker.runAndWait()
        else:
            speaker.say('Неверно')
            speaker.runAndWait()
            errors.append(m)
        arduino.close()
    speaker.say(f"Количество ошибок: {len(errors)}")
    speaker.runAndWait()
    if 8 <= len(errors) <= 10:
        speaker.say('Оценка ваших знаний - 2. Поработайте над следующими символами')
        speaker.runAndWait()
        for m in errors:
            speaker.say(m)
            speaker.runAndWait()
    elif 5 <= len(errors) <= 7:
        speaker.say('Оценка ваших знаний - 3. Поработайте над следующими символами')
        speaker.runAndWait()
        for m in errors:
            speaker.say(m)
            speaker.runAndWait()
    elif 2 <= len(errors) <= 4:
        speaker.say('Оценка ваших знаний - 4. Поработайте над следующими символами')
        speaker.runAndWait()
        for m in errors:
            speaker.say(m)
            speaker.runAndWait()
    elif 0 <= len(errors) <= 1:
        speaker.say('Оценка ваших знаний - 5. Поработайте над следующими символами')
        speaker.runAndWait()
        for m in errors:
            speaker.say(m)
            speaker.runAndWait()