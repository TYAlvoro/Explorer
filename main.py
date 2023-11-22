import yopen
import speech_recognition as sr
import pyttsx3
import phrases
import time
from vkbot import Bot
from time import sleep as sleepi
#import serial
#import random
import webbrowser
import keyboard_work
from ru_word2number import w2n
import audio_books
import radio
import brail_study
#import re
#import os
#import wikipedia
#for index, name in enumerate(sr.Microphone.list_microphone_names()):
#    print("Микрофон с именем \"{1}\" найден для `Microphone(device_index={0})`".format(index, name))


def provodnik():
    book_name = "Евгений Онегин.pdf"

    def say_sth(phrase):
        speaker.say(phrase)
        speaker.runAndWait()
        print(phrase)


    def handling(my_phrase):
        nonlocal sleep, working, assistent, voices, speaker
        if command(my_phrase, phrases.go_to_sleep):
            sleep = True
        elif command(my_phrase, phrases.adieu):
            say_sth('До свидания')
            working = False 
        elif command(my_phrase, phrases.vk_send):
            send_msg()
        elif command_rev(my_phrase, phrases.youtube_search):
            work_with_youtube(command_rev(my_phrase, phrases.youtube_search))
        elif 'выбрать книгу номер' in my_phrase:
            choose_book(my_phrase[20:])
        elif 'прочти страницу номер' in my_phrase:
            read_book(my_phrase[22:])
        elif my_phrase == 'проверить знания':
            brail_study.check_knowledge()
        elif my_phrase == 'учить шрифт':
            brail_study.studying()
        elif 'позови лизу' in my_phrase:
            assistent = 2
            speaker.setProperty("voice", voices[3].id)
            speaker.setProperty("rate", 150) 
        elif 'позови лютика' in my_phrase:
            assistent = 1
            speaker.setProperty("voice", voices[2].id)
            speaker.setProperty("rate", 205)
        elif 'включи радио' in my_phrase:
            my_phrase = my_phrase[13:]
            radio_name = my_phrase[:my_phrase.find('на')].strip()
            my_phrase = my_phrase[my_phrase.find('на') + 3:]
            num, name = w2n.word_to_num(my_phrase.split()[0]), my_phrase.split()[1]
            if 'мин' in name:
                num *= 60
            elif 'час' in name:
                num *= 3600
            radio.play_radio(radio_name, num)
            sleepi(1)


    def read_book(num):
        nonlocal book_name
        num = w2n.word_to_num(num)
        audio_books.read_page(num - 1, book_name)


    def choose_book(num):
        nonlocal book_name
        book_name = ""
        num = w2n.word_to_num(num)
        with open('books.txt', 'r', encoding='utf-8') as f:
            books = [x.strip() for x in f]
        book_name += f"{books[num - 1]}.pdf"


    def find_friend(adressee):
        with open('friends.txt', encoding='utf-8') as f:
            friends = [x.strip().split() for x in f]
        for m in friends:
            if adressee[:3] in m[0].lower():
                return m[1]

        
    def send_msg():
        nonlocal bot
        nonlocal speaker
        running = True
        say_sth('Окей')
        say_sth('Какой ввод будет использоваться')
        recognizer = sr.Recognizer()
        with sr.Microphone(device_index=1) as source:
            audio = recognizer.listen(source)
        input = recognizer.recognize_google(audio, language="ru-RU")
        if input == 'голосовой':
            say_sth('С кем хотите общаться?')
            with sr.Microphone(device_index=1) as source:
                audio = recognizer.listen(source)
            adressee = recognizer.recognize_google(audio, language="ru-RU")
            say_sth('Будем общаться ' + adressee)
            if adressee != "с самим собой":
                adressee = find_friend(adressee.split()[1])
            else:
                adressee = "638763302"
            while running:
                speaker.setProperty('rate', 205)
                say_sth('Продиктуйте текст сообщения')
                with sr.Microphone(device_index=1) as source:
                    audio = recognizer.listen(source)
                msg_text = recognizer.recognize_google(audio, language="ru-RU")
                if msg_text == 'прекратить общение':
                    say_sth('Окей')
                    running = False
                    break
                bot.send_msg(adressee, msg_text)
                say_sth('Сообщение отправлено')
                say_sth('Жду ответа')
                ans = bot.get_msg_text()
                say_sth('Вам ответили')
                sleepi(1)
                speaker.setProperty('rate', 170)
                say_sth(ans)
                sleepi(2)
        elif input == 'ручной':
            say_sth('С кем хотите общаться?')
            with sr.Microphone(device_index=1) as source:
                audio = recognizer.listen(source)
            adressee = recognizer.recognize_google(audio, language="ru-RU")
            say_sth('Будем общаться ' + adressee)
            if adressee != "с самим собой":
                adressee = find_friend(adressee.split()[1])
            else:
                adressee = "638763302"
            while running:
                say_sth('Напечатайте новое сообщение')
                msg_text = keyboard_work.make_message()
                say_sth('Ваше сообщение')
                sleepi(0.5)
                say_sth(msg_text)
                bot.send_msg(adressee, msg_text)
                say_sth('Сообщение отправлено')
                say_sth('Жду ответа')
                ans = bot.get_msg_text()
                say_sth('Вам ответили')
                sleepi(1)
                say_sth(ans)
                sleepi(1)
                with sr.Microphone(device_index=1) as source:
                    audio = recognizer.listen(source)
                if recognizer.recognize_google(audio, language="ru-RU") == 'прекратить общение':
                    say_sth('Окей')
                    running = False
                    break                


    def work_with_youtube(searching):
        say_sth('Вам открыть первое видео или просто поискать?')
        recognizer = sr.Recognizer()
        with sr.Microphone(device_index=1) as source:
            audio = recognizer.listen(source)
        ans = recognizer.recognize_google(audio, language="ru-RU").lower()
        if ans == 'открыть':    
            yopen.search_in_youtube(searching)
        else:
            webbrowser.open('https://www.youtube.com/results?search_query=' + searching)


    def sleeping(my_phrase):
        nonlocal sleep
        if command(my_phrase, phrases.wake_up):
            sleep = False


    def command(my_phrase, listi):
        for m in listi:
            if my_phrase == m:
                return True
        return False


    def command_rev(my_phrase, listi):
        for m in listi:
            if m in my_phrase:
                return my_phrase[len(m) + 1:]


    speaker = pyttsx3.init()
    voices = speaker.getProperty("voices") 
    assistent = 1
    if assistent == 1:
        speaker.setProperty("voice", voices[2].id)
        speaker.setProperty("rate", 205)
    else:
        speaker.setProperty("voice", voices[3].id)
        speaker.setProperty("rate", 150) 
    recognizer = sr.Recognizer()
    sleep = False
    working = True
    bot = Bot()

    while working:
        try:
            with sr.Microphone(device_index=1) as source:
                if not(sleep):
                    if assistent == 1:
                        say_sth("Лютик к твоим услугам")
                    else:
                        say_sth("Лиза готова к работе")
                else:
                    print("Я сплю")
                audio = recognizer.listen(source)
            my_phrase = recognizer.recognize_google(audio, language="ru-RU").lower()
            print(my_phrase.lower())

            if not(sleep):
                handling(my_phrase)
            else:
                sleeping(my_phrase)
        except Exception as e:
            print(e)