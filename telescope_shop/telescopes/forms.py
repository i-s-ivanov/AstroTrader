from django import forms
from django.core.validators import MinValueValidator, MinLengthValidator, MaxLengthValidator

from telescope_shop.telescopes.models import Telescope, Comment


class CreateTelescopeForm(forms.ModelForm):
    make = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    model = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(required=True, widget=forms.Textarea(attrs={'class': 'form-control'}))
    price = forms.IntegerField(required=True, validators=[MinValueValidator(0)], widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'type': 'number'
        }
    ))
    image = forms.ImageField(required=True, widget=forms.FileInput(attrs={'class': 'form-control'}))
    location = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    contact_number = forms.CharField(required=True, widget=forms.NumberInput(attrs={'class': 'form-control'}),
                                     validators=[MinLengthValidator(10), MaxLengthValidator(10)])

    class Meta:
        model = Telescope
        fields = ('make', 'model', 'description', 'price', 'location', 'contact_number', 'image',)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'text',)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control'}),
        }
