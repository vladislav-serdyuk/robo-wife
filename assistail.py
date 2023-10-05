# Голосовой ассистент КЕША 1.0 BETA
import os
import time
import datetime
import webbrowser
import random
import types
import importlib

import speech_recognition as sr  # запись звука и рапознавание речи
from fuzzywuzzy import fuzz  # нечёткое сравнение
import pyttsx3  # воспроизведение текста
import wikipedia

import freeGPT
from asyncio import run

gpt = freeGPT.gpt3.Completion()

# настройки
opts = {
    "alias": ('масяня', 'мось', 'мася'),
    "tbr": ('скажи', 'расскажи', 'покажи', 'сколько', 'произнеси'),
    "cmds": [
        ("ctime", ('текущее время', 'сейчас времени', 'который час')),
        ("stupid1", ('анекдот', 'рассмеши меня', 'ты знаешь анекдоты')),
        ("openCode", ('открой код', 'открой программу')),
        ("openGoogle", ('открой google', 'открой интернет')),
        ("wikipedia", ('wikipedia', 'википедия', 'вики', 'wiki')),
        ('open youtube', ('youtube', 'открой youtube')),
        ('open stackoverflow', ('stack overflow', 'открой stack overflow')),
        ('bye', ('пока', 'досвидание', 'bye', 'good', 'до встречи')),
    ]
}


user = 'user'
system = 'system'
assistant = 'assistant'


# функции
def speak(what: str) -> None:
    print(what)
    speak_engine.say(what)
    speak_engine.runAndWait()
    speak_engine.stop()


def callback(recognizer: sr.Recognizer, audio):
    try:
        voice: str = recognizer.recognize_google(audio, language="ru-RU").lower()

        print("[log] Распознано: " + voice)

        if voice.startswith(opts["alias"]):
            # обращаются к Кеше

            prepared_voice = voice

            for x in opts['alias']:
                prepared_voice = prepared_voice.replace(x, "").strip()

            for x in opts['tbr']:
                prepared_voice = prepared_voice.replace(x, "").strip()

            # распознаем и выполняем команду
            cmd = recognize_cmd(prepared_voice)
            execute_cmd(cmd)

    except sr.UnknownValueError:
        print("[log] Голос не распознан!")
    except sr.RequestError:
        print("[log] Неизвестная ошибка, проверьте интернет!")


def recognize_cmd(cmd: str) -> str:
    """
    распознавание команды
    :param cmd: команда
    :return: {'cmd': команда, 'percent': соответствие}
    """
    RC = {'cmd': cmd, 'percent': 48}
    for c, v in opts['cmds']:
        for x in v:
            vrt = fuzz.ratio(cmd, x)
            if vrt > RC['percent']:
                RC['cmd'] = c
                RC['percent'] = vrt
    return RC['cmd']


def execute_cmd(cmd: str | types.FunctionType) -> None:
    """
    Выполняет команду
    :param cmd: соманда, str or func
    :return: None
    """

    if isinstance(cmd, types.FunctionType):
        cmd(speak)
        return

    if cmd == 'ctime':
        # сказать текущее время
        now = datetime.datetime.now()
        speak(f"Сейчас {now.strftime('%H:%M')}")

    elif cmd == 'stupid1':
        # рассказать анекдот
        speak("Мой разработчик не научил меня анекдотам ... Ха ха ха")

    elif cmd == 'openCode':
        os.system(r"C:\\Users\\User\\PycharmProjects\\robowife\\main.py")

    elif cmd == 'openGoogle':
        webbrowser.open('www.google.com')

    elif cmd == 'wikipedia':
        speak('поиск в викепедии...')
        query = random.choice(['Wikipedia', 'openAI', 'chatGPT_'])
        results = wikipedia.summary(query, sentences=5)
        speak("в вике найдено")
        print(results)
        speak(results)

    elif cmd == 'open youtube':
        webbrowser.open("youtube.com")

    elif cmd == 'open stackoverflow':
        webbrowser.open("stackoverflow.com")

    elif cmd == 'calc':
        speak('Научись уже пользоваться калькулятором')

    elif cmd == 'bye':
        speak('До свидания')
        exit()

    elif cmd == '':
        print('[log] No command: cmd = ""')

    else:
        res = run(gpt.create(cmd))
        speak(res)


def add_extensions():
    for file_name in os.listdir(path='extensions'):
        if len(file_name) < 3 or file_name[-3:] != '.py':  # if it's not python file
            continue
        module = importlib.import_module(f'extensions.{file_name[:-3]}')  # без .py
        if 'command' in dir(module):  # если в модуле есть command: tuple[_f, tuple[str]], то
            opts['cmds'].append(module.command)  # add extension


def start() -> None:
    """
    Здоровается и наченает прослушку
    :return: None
    """
    speak('С использаванием GPT3')
    speak("Добрый день, повелитель")
    speak("Масяня слушает")

    r.listen_in_background(m, callback)


def mainloop() -> None:
    """
    Бесконечный цикл
    :return: None
    """
    while True:
        time.sleep(0.1)  # infinity loop


# запуск
r = sr.Recognizer()
m = sr.Microphone(device_index=1)

with m as source:
    r.adjust_for_ambient_noise(source)

speak_engine = pyttsx3.init()

# Только если у вас установлены голоса для синтеза речи!
voices = speak_engine.getProperty('voices')
speak_engine.setProperty('voice', voices[0].id)

add_extensions()

if __name__ == '__main__':
    start()
    mainloop()
