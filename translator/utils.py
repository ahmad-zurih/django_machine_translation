from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, pipeline
import torch
from django.conf import settings

def load_model():
    model_path = settings.MODEL_PATH
    model = AutoModelForSeq2SeqLM.from_pretrained(model_path)
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model.to(device)
    return model, tokenizer

def translate_sentence(sentence, model, tokenizer):
    """
    Translate a given sentence from English to German.
    """
    # Create a translation pipeline
    translator = pipeline("translation_en_to_de", model=model, tokenizer=tokenizer, device=torch.cuda.current_device() if torch.cuda.is_available() else -1)
    # Translate the sentence
    translation = translator(sentence)
    return translation[0]['translation_text']

model, tokenizer = load_model()
