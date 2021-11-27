from django import forms
from . models import Country

class CountryDataForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = '__all__'