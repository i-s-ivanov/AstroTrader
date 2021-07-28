from django.urls import path

from telescope_shop.common.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]