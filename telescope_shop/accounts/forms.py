from django import forms
from django.contrib.auth import get_user_model

from telescope_shop.accounts.models import Profile
from telescope_shop.common.forms import BootstrapFormMixin

UserModel = get_user_model()


class ProfileForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('profile_image',)


