from django import forms
from django.forms import SelectDateWidget
from .models import Category


class DateForm(forms.Form):
    asked_date = forms.DateField(label='Выберите дату ', widget=SelectDateWidget)
    asked_cat = forms.ModelChoiceField(required=False, label='Выберите категорию', queryset=Category.objects.all())
