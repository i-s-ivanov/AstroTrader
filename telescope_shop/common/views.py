from django.db.models import Q
from django.views import generic


from telescope_shop.telescopes.models import Telescope


class IndexView(generic.TemplateView):
    template_name = 'home.html'


class SearchResultsView(generic.ListView):
    model = Telescope
    template_name = 'search_result.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Telescope.objects.filter(
            Q(make__icontains=query) | Q(model__icontains=query)
        )
        return object_list
