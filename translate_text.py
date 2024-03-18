import os
from dotenv import load_dotenv
import deepl

load_dotenv()
# Ваш ключ API от DeepL
auth_key = os.getenv('DEEPL_API_KEY')

if not auth_key:
    raise ValueError("Не удалось загрузить ключ API DeepL из переменных среды.")

translator = deepl.Translator(auth_key)

def translate(text_to_translate, target_lang="EN-US"):
    if not isinstance(text_to_translate, str) or text_to_translate.strip() == "":
        print("Передан пустой текст для перевода.")
        return ""
    result = translator.translate_text(text=text_to_translate, target_lang=target_lang)
    return result.text
