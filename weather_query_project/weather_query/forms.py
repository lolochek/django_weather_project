from django import forms

class CityNameForm(forms.Form):
    city_name = forms.CharField(label='Enter city name', max_length=100, required=True)