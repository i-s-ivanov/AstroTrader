from django.contrib.auth import get_user_model

# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from telescope_shop.common.forms import BootstrapFormMixin
from telescope_shop.telescopes.forms import CreateTelescopeForm, CommentForm
from telescope_shop.telescopes.models import Telescope, Comment

UserModel = get_user_model()


class TelescopeListView(generic.ListView):
    template_name = 'telescopes/telescope_list.html'
    model = Telescope
    context_object_name = 'telescopes'
    ordering = ['-created']
    paginate_by = 6


class TelescopeDetails(generic.DetailView):
    model = Telescope
    template_name = 'telescopes/telescope_details.html'

    def get_context_data(self, **kwargs):
        context = super(TelescopeDetails, self).get_context_data(**kwargs)
        context['is_owner'] = self.object.user_id == self.request.user.id
        return context


class CommentView(generic.CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'telescopes/telescope_comment.html'

    def get_success_url(self):
        item_id = self.kwargs['pk']
        return reverse_lazy('telescope details', kwargs={'pk': item_id})

    def form_valid(self, form):
        form.instance.telescope_id = self.kwargs['pk']
        return super().form_valid(form)




class TelescopeCreateView(BootstrapFormMixin, LoginRequiredMixin, generic.CreateView):
    form_class = CreateTelescopeForm
    model = Telescope
    template_name = 'telescopes/telescope_create.html'
    success_url = reverse_lazy('telescope list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TelescopeUpdateView(BootstrapFormMixin, generic.UpdateView):
    model = Telescope
    template_name = 'telescopes/telescope_update.html'
    fields = ('make', 'model', 'description', 'price', 'image')

    def get_success_url(self):
        item_id = self.kwargs['pk']
        return reverse_lazy('telescope details', kwargs={'pk': item_id})


class TelescopeDeleteView(generic.DeleteView):
    fields = '__all__'
    model = Telescope
    template_name = 'telescopes/telescope_delete.html'
    success_url = reverse_lazy('telescope list')
