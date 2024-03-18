from record_audio import record
from speech_to_text import speech_to_text
from translate_text import translate
from text_to_speech import speak
from user_text_input import get_user_text  # Добавьте этот импорт

def main():
    print("Добро пожаловать в голосовой переводчик!")

    # Запрос языков перевода
    source_lang = input("Введите язык оригинала (например, ru-RU): ")
    target_lang = input("Введите целевой язык для перевода (например, en-US): ")

    # Спрашиваем у пользователя, хочет ли он ввести текст или использовать голосовой ввод
    input_type = input("Хотите ввести текст или использовать голосовой ввод? (текст/голос): ")

    if input_type.lower() == 'голос':
        print("Пожалуйста, говорите после сигнала. Программа записывает вашу речь...")
        audio_path = "output.wav"  # Записываем голос пользователя
        record(WAVE_OUTPUT_FILENAME=audio_path)  # Записываем голос пользователя
        print("Запись завершена. Идет распознавание и перевод...")
    
        # Преобразование из голоса в текст
        text = speech_to_text(audio_path=audio_path, source_lang=source_lang)
    elif input_type.lower() == 'текст':
        # Получаем текст от пользователя
        text = get_user_text()
    else:
        print("Нераспознанный тип ввода. Пожалуйста, введите 'текст' или 'голос'.")
        return

    if text == "Распознание не удалось.":
        print("Распознать текст не удалось")
        return 
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
