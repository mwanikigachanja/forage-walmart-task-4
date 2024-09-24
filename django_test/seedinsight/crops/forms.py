from django import forms
from .models import Seed

class CropForm(forms.ModelForm):
    class Meta:
        model = Seed
        fields = ['crop', 'variety', 'altitude_zone', 'maturity', 'rate', 'yield_per_acre', 'attributes']
