import speech_recognition as sr

# Создаем экземпляр распознавателя
recognizer = sr.Recognizer()

# Путь к аудиофайлу
audio_file = "/home/ubuntu/opt/labs/output.wav"

def speech_to_text(audio_path, source_lang):
    # Открываем файл для записи результата
    with open('text.txt', 'w') as file:
        # Используем аудиофайл в качестве источника
        with sr.AudioFile(audio_path) as source:
            print("Обработка аудиофайла...")
            # Записываем аудио из файла
            audio_data = recognizer.record(source)
            # Пытаемся распознать аудио
            text = ""
            try:
                text = recognizer.recognize_google(audio_data, language=source_lang)
                file.write(text + '\n')
                print("Текст аудиофайла: " + text)
            except sr.UnknownValueError:
                print("Google Web Speech API не смогла распознать аудио.")
                text = "Распознание не удалось."
            except sr.RequestError as e:
                print(f"Не удалось отправить запрос на Google Web Speech API; {e}")
                text = "Ошибка передачи данных."
            return text

if __name__ == "__main__":
    speech_to_text(audio_file)
