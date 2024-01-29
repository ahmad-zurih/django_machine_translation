from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import TranslationForm
from .utils import model, tokenizer, translate_sentence
import json


def home(request):
    form = TranslationForm()
    return render(request, 'translator/home.html', {'form': form})



@csrf_exempt
def translate_ajax(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        sentence = data.get('text', '')
        if sentence:
            translation = translate_sentence(sentence, model, tokenizer)
            return JsonResponse({'translation': translation})
        else:
            return JsonResponse({'error': 'No text provided'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request'}, status=400)


def source_code(request):
    return render(request, 'translator/source_code.html')