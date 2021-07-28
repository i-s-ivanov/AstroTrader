from django import forms
from django.core.validators import MinValueValidator

from telescope_shop.telescopes.models import Telescope


class CreateTelescopeForm(forms.ModelForm):
    make = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control'
        }
    ))
    model = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control'
        }
    ))
    description = forms.CharField(required=True, widget=forms.Textarea(
        attrs={
            'class': 'form-control'
        }
    ))
    price = forms.IntegerField(required=True,
                               validators=[MinValueValidator(0)],
                               widget=forms.TextInput(
                                   attrs={
                                       'class': 'form-control',
                                       'type': 'number'
                                   }
                               ))
    image = forms.ImageField(required=True, widget=forms.FileInput(
        attrs={
            'class': 'form-control'
        }
    ))

    class Meta:
        model = Telescope
        fields = ('make', 'model', 'description', 'price', 'image')
