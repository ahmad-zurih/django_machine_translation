from django import forms

class TranslationForm(forms.Form):
    sentence = forms.CharField(label='Enter a sentence in English', max_length=200)
