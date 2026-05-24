from django.urls import path
from .views import *

urlpatterns = [
    path('', AlbumListView.as_view(), name='album-list'),
    path('create/', AlbumCreateView.as_view(), name='album-create'),
    path('<int:pk>/', AlbumDetailView.as_view(), name='album-detail'),
    path('<int:pk>/update/', AlbumUpdateView.as_view(), name='album-update'),
    path('<int:pk>/delete/', AlbumDeleteView.as_view(), name='album-delete'),
]