from django.urls import path

from telescope_shop.common.views import IndexView, SearchResultsView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('search/', SearchResultsView.as_view(), name='search results'),

]
