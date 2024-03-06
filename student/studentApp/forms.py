from django import forms
from .models import section

class sectionform(forms.ModelForm):
    class Meta:
        model = section
        fields = '__all__'
