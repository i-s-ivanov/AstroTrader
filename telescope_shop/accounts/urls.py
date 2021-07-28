from django.urls import path

from telescope_shop.accounts.views import RegisterView, LogoutView, LoginVew, profile_details

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginVew.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', profile_details, name='profile details'),
]
