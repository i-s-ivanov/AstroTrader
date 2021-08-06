from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView

# Create your views here.
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import views as auth_views, login, get_user_model
from django.contrib.auth import forms as auth_forms
from django.views.generic import FormView

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


class ProfileDetailsView(FormView):
    template_name = 'auth/profile_details.html'
    form_class = ProfileForm
    success_url = reverse_lazy('profile details')
    object = None

    def get(self, request, *args, **kwargs):
        self.object = Profile.objects.get(pk=self.request.user.id)
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = Profile.objects.get(pk=self.request.user.id)
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        self.object.profile_image = form.cleaned_data['profile_image']
        self.object.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_posts = Telescope.objects.filter(user_id=self.request.user.id)
        context['posts'] = user_posts
        context['profile'] = self.object
        return context
