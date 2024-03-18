from gtts import gTTS
import os

def speak(text, language='en'):
    # Нет необходимости перезаписывать параметр language, так как он уже получает значение по умолчанию

    # Создаем объект gTTS
    tts = gTTS(text=text, lang=language, slow=False)

    # Сохраняем аудиофайл
    tts.save("result.mp3")

    # Воспроизведение аудио файла. Определение запуска в зависимости от ОС
    if os.name == 'nt':  # Для Windows
        os.system("start result.mp3")
    elif os.name == 'posix':  # Для Unix/Linux/MacOS
        try:
            # Пытаемся использовать mpg321 для Linux
            os.system("mpg321 result.mp3")
        except:
            # Используем afplay для MacOS, если mpg321 не найден
            os.system("afplay result.mp3")
    else:
        print("Unsupported OS")
