from django import forms
from .models import DictionaryDb

class DictionaryForm(forms.ModelForm):
    class Meta:
        model=DictionaryDb
        fields=['letter','word','definition','example']
