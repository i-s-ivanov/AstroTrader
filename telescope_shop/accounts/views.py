from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import views as auth_views, login
from django.contrib.auth import forms as auth_forms

from telescope_shop.accounts.forms import ProfileForm
from telescope_shop.accounts.models import Profile
from telescope_shop.common.forms import BootstrapFormMixin
from telescope_shop.telescopes.models import Telescope


class RegisterView(BootstrapFormMixin, generic.CreateView):
    form_class = auth_forms.UserCreationForm
    template_name = 'auth/register.html'
    success_url = reverse_lazy('telescope list')

    def form_valid(self, form):
        valid = super().form_valid(form)
        user = form.save()
        login(self.request, user)
        return valid


class LoginVew(BootstrapFormMixin, auth_views.LoginView):
    template_name = 'auth/login.html'


class LogoutView(auth_views.LogoutView):
    next_page = reverse_lazy('index')


def profile_details(request):
    profile = Profile.objects.get(pk=request.user.id)
    if request.method == 'POST':
        form = ProfileForm(
            request.POST,
            request.FILES,
            instance=profile,
        )
        if form.is_valid():
            form.save()
            return redirect('profile details')
    else:
        form = ProfileForm(instance=profile)

    user_ads = Telescope.objects.filter(user_id=request.user.id)

    context = {
        'form': form,
        'ads': user_ads,
        'profile': profile,
    }

    return render(request, 'auth/profile_details.html', context)
