# robo-wife

### libraries:
- SpeechRecognition
- fuzzywuzzy
- pyttsx3
- PyAudio
- pywin32
- pypiwin32
- wikipedia
- freeGPT
- cv2
- cv3-beta

### extensions
Для добавления расширения
создайте папку extensions
и поестите python файл формата

>def run(speak, sw_status):  # speak and sw_status are functions, example: speak('Good')
>  ...
>
>command = {'main': [
>                     (run, ('string1', 'string2', ...)),
>                      ...
>                   ],
>           'light on':[...]
>          }  # эта переменая обезательна
>             # string - как вызывать команду, пример:
>             # (run, ('turn on light', 'включи лампу', ...))
>
