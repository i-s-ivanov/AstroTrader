from django.urls import path

from telescope_shop.telescopes.views import TelescopeListView, TelescopeDetails, TelescopeCreateView, TelescopeUpdateView, TelescopeDeleteView

urlpatterns = [
    path('', TelescopeListView.as_view(), name='telescope list'),
    path('details/<int:pk>/', TelescopeDetails.as_view(), name='telescope details'),
    path('create/', TelescopeCreateView.as_view(), name='create telescope'),
    path('update/<int:pk>/', TelescopeUpdateView.as_view(), name='update telescope'),
    path('delete/<int:pk>', TelescopeDeleteView.as_view(), name='delete telescope'),
]
