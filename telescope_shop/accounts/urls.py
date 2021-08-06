from django.contrib.auth.views import PasswordChangeView
from django.urls import path

from telescope_shop.accounts.views import RegisterUserView, LogoutView, LoginVew, UpdateUserView, \
    PasswordsChangeView, DeleteUserView, ProfileDetailsView

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('update/', UpdateUserView.as_view(), name='update profile'),
    path('login/', LoginVew.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', ProfileDetailsView.as_view(), name='profile details'),
    path('password/', PasswordsChangeView.as_view(), name='change password'),
    path('delete/<int:pk>/', DeleteUserView.as_view(), name='delete profile'),

]
