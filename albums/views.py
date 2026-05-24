from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView
)

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Album

class AlbumListView(LoginRequiredMixin, ListView):
    model = Album
    template_name = 'albums/album_list.html'

class AlbumCreateView(LoginRequiredMixin, CreateView):
    model = Album
    fields = ['title', 'description', 'image']
    success_url = reverse_lazy('album-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class AlbumUpdateView(LoginRequiredMixin, UpdateView):
    model = Album
    fields = ['title', 'description', 'image']
    success_url = reverse_lazy('album-list')

class AlbumDeleteView(LoginRequiredMixin, DeleteView):
    model = Album
    success_url = reverse_lazy('album-list')

class AlbumDetailView(LoginRequiredMixin, DetailView):
    model = Album