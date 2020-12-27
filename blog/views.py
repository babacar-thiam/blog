from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Post


class HomePageView(ListView):
    model = Post
    template_name = 'index.html'


class DetailPageView(DetailView):
    model = Post
    template_name = 'detail.html'


class CreatePageView(CreateView):
    model = Post
    template_name = 'new_post.html'
    fields = '__all__'


class UpdatePageView(UpdateView):
    model = Post
    template_name = 'edit_post.html'
    fields = ['title', 'body']


class DeletePageView(DeleteView):
    model = Post
    template_name ='delete_post.html'
    success_url = reverse_lazy('index')
