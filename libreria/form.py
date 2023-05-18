from dataclasses import field
from django import forms
from django import forms
from .models import libro

class libroform(forms.ModelForm):
    class Meta:
        model = libro
        fields = '__all__'