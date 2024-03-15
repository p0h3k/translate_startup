# Импорт необходимых модулей
from record_audio import record
from speech_to_text import speech_to_text
from translate_text import translate
from text_to_speech import speak

def main():
    print("Добро пожаловать в голосовой переводчик!")

    # Запрос языков перевода
    source_lang = input("Введите язык оригинала (например, ru-RU): ")
    target_lang = input("Введите целевой язык для перевода (например, en-US): ")
    
    print("Пожалуйста, говорите после сигнала. Программа записывает вашу речь...")
    audio_path = "output.wav"  # Записываем голос пользователя
    record(WAVE_OUTPUT_FILENAME=audio_path)  # Записываем голос пользователя
    print("Запись завершена. Идет распознавание и перевод...")
    
    # Преобразование из голоса в текст
    text = speech_to_text(audio_path=audio_path, source_lang=source_lang)
    print(f"Распознанный текст: {text}")
    
    # Перевод текста на целевой язык
    translated_text = translate(text_to_translate=text, target_lang=target_lang)
    print(f"Переведенный текст: {translated_text}")
    
    # Опциональное воспроизведение голосом
    should_speak = input("Хотите воспроизвести переведенный текст голосом? (да/нет): ")
    if should_speak.lower() in ('да', 'yes'):
        speak(text=translated_text, language=target_lang[:2])
 
    print("Спасибо за использование нашего переводчика!")

if __name__ == "__main__":
    main()
