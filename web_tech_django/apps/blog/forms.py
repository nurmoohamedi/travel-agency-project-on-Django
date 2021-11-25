from .models import Tour
from django.forms import ModelForm, TextInput, Textarea, NumberInput, DateInput


class TourForm(ModelForm):
    class Meta:
        model = Tour
        fields = ("name", "description", "started", "price", "duration")
        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Enter the name'
            }),
            "description": Textarea(attrs={
                'class': 'form-control', 'placeholder': 'Enter the description'
            }),
            "started": DateInput(attrs={
                'class': 'form-control', 'placeholder': 'Enter started date', 'type': 'date'
            }),
            "price": NumberInput(attrs={
                'class': 'form-control', 'placeholder': 'Enter price of the tour'
            }),
            "duration": NumberInput(attrs={
                'class': 'form-control', 'placeholder': 'Enter duration'
            }),
        }
