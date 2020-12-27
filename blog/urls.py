from os import name
from django.urls import path

from .views import HomePageView, DetailPageView, CreatePageView, UpdatePageView, DeletePageView


urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
    path('post/<int:pk>', DetailPageView.as_view(), name='detail'),
    path('post/new/', CreatePageView.as_view(), name='new_post'),
    path('post/<int:pk>/edit/', UpdatePageView.as_view(), name='edit_post'),
    path('post/<int:pk>/delete/', DeletePageView.as_view(), name='delete_post'),
]
