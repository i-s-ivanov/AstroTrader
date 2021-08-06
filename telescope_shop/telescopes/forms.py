from django import forms
from django.core.validators import MinValueValidator, MinLengthValidator, MaxLengthValidator

from telescope_shop.telescopes.models import Telescope, Comment
from mptt.forms import TreeNodeChoiceField


class CreateTelescopeForm(forms.ModelForm):
    make = forms.CharField(max_length=100, required=True, widget=forms.TextInput())
    model = forms.CharField(max_length=100, required=True, widget=forms.TextInput())
    description = forms.CharField(max_length=250, required=True, widget=forms.Textarea())
    price = forms.IntegerField(required=True, validators=[MinValueValidator(0)], widget=forms.TextInput(
        attrs={
            'type': 'number'
        }
    ))
    image = forms.ImageField(required=True, widget=forms.FileInput())
    location = forms.CharField(max_length=50, required=True, widget=forms.TextInput())
    contact_number = forms.CharField(required=True, widget=forms.NumberInput(),
                                     validators=[MinLengthValidator(10), MaxLengthValidator(10)])

    class Meta:
        model = Telescope
        fields = ('make', 'model', 'description', 'price', 'location', 'contact_number', 'image',)


class CommentForm(forms.ModelForm):
    parent = TreeNodeChoiceField(queryset=Comment.objects.all())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['parent'].required = False
        self.fields['parent'].label = ''
        self.fields['parent'].widget.attrs.update(
            {'class': 'd-none'}
        )

    class Meta:
        model = Comment
        fields = ('name', 'parent', 'text',)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'col-sm-12'}),
            'text': forms.Textarea(attrs={'class': 'form-control'}),
        }
