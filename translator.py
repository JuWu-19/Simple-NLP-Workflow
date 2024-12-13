# translator.py
from transformers import MarianMTModel, MarianTokenizer
import re

# Load MarianMT model for zh->en translation once at import
model_name = 'Helsinki-NLP/opus-mt-zh-en'
tokenizer = MarianTokenizer.from_pretrained(model_name)
translation_model = MarianMTModel.from_pretrained(model_name)

def contains_chinese(text):
    # Check if there's at least one Chinese character
    return bool(re.search('[\u4e00-\u9fff]+', text))

def translate_to_english(text):
    text = text.strip()
    if not text:
        return text
    # If the text contains Chinese, translate it
    if contains_chinese(text):
        tokens = tokenizer([text], return_tensors="pt")
        translated = translation_model.generate(**tokens)
        english_text = tokenizer.decode(translated[0], skip_special_tokens=True)
        return english_text
    else:
        return text  # If no Chinese text, return as-is
