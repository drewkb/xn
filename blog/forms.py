from django import forms
from django.forms import SelectDateWidget


class DateForm(forms.Form):
    asked_date = forms.DateField(widget=SelectDateWidget)

