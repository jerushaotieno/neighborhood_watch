from django import forms
from .models import Neighborhood, Business


# Neighborhood Form

class NeighborhoodForm(forms.ModelForm):
    class Meta:
        model = Neighborhood
        exclude = ('admin',)


# Business Form

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ('user', 'neighbourhood')
