from gtts import gTTS
import os


def speak(text,language='en'):
	language = 'en'

# Создаем объект gTTS
	tts = gTTS(text=text, lang=language, slow=False)

# Сохраняем аудиофайл
	tts.save("result.mp3")

# Воспроизведение аудиофайла, если необходимо
# Для macOS
#os.system("afplay output.mp3")
# Для Windows
# os.system("start output.mp3")
# Для Linux
	os.system("mpg321 result.mp3")

