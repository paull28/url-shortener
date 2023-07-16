from django import forms
from .models import *

class urlForm(forms.ModelForm):
    class Meta:
        model = url
        fields = ['source', 'new']
        widgets = {
            'source': forms.TextInput(attrs={
                'class': 'formfield',
                'placeholder': 'Original URL',
            }),
            'new' : forms.TextInput(attrs={
                'class': 'formfield',
                'placeholder': 'New Identifier',
            }),
        }
