from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import views as auth_views, login, get_user_model
from django.contrib.auth import forms as auth_forms

from telescope_shop.accounts.forms import ProfileForm, UserUpdateForm
from telescope_shop.accounts.models import Profile
from telescope_shop.common.forms import BootstrapFormMixin
from telescope_shop.telescopes.models import Telescope

UserModel = get_user_model()


class RegisterUserView(BootstrapFormMixin, generic.CreateView):
    form_class = auth_forms.UserCreationForm
    template_name = 'auth/register.html'
    success_url = reverse_lazy('telescope list')

    def form_valid(self, form):
        valid = super().form_valid(form)
        user = form.save()
        login(self.request, user)
        return valid


class UpdateUserView(BootstrapFormMixin, generic.UpdateView):
    form_class = UserUpdateForm
    template_name = 'auth/update.html'
    success_url = reverse_lazy('profile details')

    def get_object(self, queryset=None):
        return self.request.user


class DeleteUserView(generic.DeleteView):
    fields = '__all__'
    model = UserModel
    template_name = 'auth/delete.html'
    success_url = reverse_lazy('index')


class LoginVew(BootstrapFormMixin, auth_views.LoginView):
    template_name = 'auth/login.html'


class LogoutView(auth_views.LogoutView):
    next_page = reverse_lazy('index')


class PasswordsChangeView(BootstrapFormMixin, PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('profile details')
    template_name = 'auth/user_password_change.html'


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

    user_posts = Telescope.objects.filter(user_id=request.user.id)

    context = {
        'form': form,
        'posts': user_posts,
        'profile': profile,
    }

    return render(request, 'auth/profile_details.html', context)
