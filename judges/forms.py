from django import forms
from django.forms.widgets import SelectMultiple
from .models import Example

class ExampleForm(forms.widgets.Select):
    class Meta:
        model = Example
        fields = "__all__"
        exclude = ("content_type", "problem", )