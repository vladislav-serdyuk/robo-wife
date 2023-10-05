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

>def run(speak):  # speak is functions, example: speak('Good')
>  ...
>
>command = (run, ('string1', 'string2', ...))  # эта переменая обезательна
>                                              # string - как вызывать команду, пример:
>                                              # (run, ('turn on light', 'включи лампу', ...))
>
