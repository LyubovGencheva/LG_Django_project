from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from . models import Post

def home(request):
    context = {
        'posts': Post.objects.all(),
    }
    return render(request, 'blog/home.html', context)


# ListView for the homepage instead of function
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'    # if we do not have template_name variable, by default django's class based view
                                        # will search for a template <app>/<model>_<viewtype>.html (i.e. blog/post_list.html
    context_object_name = 'posts'
    ordering = ['-date_posted']          # ordering; if from oldest to newest ['date_posted']


# DetailView for each post
class PostDetailView(DetailView):
    model = Post


# CreateView for a post will contain a form, that is why the form fields have to be specified
# LoginRequiredMixin will now allow a user to create a post unless he is logged in
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    # overriding the form save method: will take the user, making the request and set it to be the post's author
    def form_valid(self, form):
        form.instance.author = self.request.user        # setting the author before checking form validity
        return super().form_valid(form)                 # running the form_valid method on the parent class


# CreateView for a post will contain a form, that is why the form fields have to be specified
# LoginRequiredMixin will now allow a user to create a post unless he is logged in
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields =['title', 'content']

    # overriding the form save method: will take the user, making the request and set it to be the post's author
    def form_valid(self, form):
        form.instance.author = self.request.user        # setting the author before checking form validity
        return super().form_valid(form)                 # running the form_valid method on the parent class

    # users will only be able to update their own posts
    def test_func(self):                                # a function checking whether the user passes the required test
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


# DetailView for each post
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'                                   # in case of successful post deletion, redirect to homepage

    # users will only be able to delete their own posts
    def test_func(self):                                # a function checking whether the user passes the required test
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})  #the last variable is the context dictionary to be passed to the about template


