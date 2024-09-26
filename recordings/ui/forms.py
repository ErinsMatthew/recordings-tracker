from django import forms


class LocationForm(forms.Form):
    name = forms.CharField(label="Location Name", max_length=128)
    city = forms.CharField(label="City Name", max_length=128)
