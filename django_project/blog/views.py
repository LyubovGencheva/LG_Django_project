from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
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
    template_name = 'blog/home.html'            # if we do not have template_name variable, by default django's class based view
                                                # will search for a template <app>/<model>_<viewtype>.html (i.e. blog/post_list.html
    context_object_name = 'posts'
    ordering = ['-date_posted']                 # ordering; if from oldest to newest ['date_posted']
    paginate_by = 5                             # 5 posts per page


# ListView for the posts by a particular user, when click-ing on his username
class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'      # if we do not have template_name variable, by default django's class based view
                                                # will search for a template <app>/<model>_<viewtype>.html (i.e. blog/post_list.html
    context_object_name = 'posts'
    paginate_by = 5                             # 5 posts per page

    # override the get_queryset method to fetch posts by a single user
    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


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


# UpdateView for a post will contain a form, that is why the form fields have to be specified
# LoginRequiredMixin will now allow a user to create a post unless he is logged in
# UserPassesTestMixin will not allow anyone, but the post author to update the post
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        if self.request.user.is_superuser:
            return super().form_valid(form)             # running the form_valid method on the parent class
        else:
            form.instance.author = self.request.user    # setting the author before checking form validity!
        return super().form_valid(form)                 # running the form_valid method on the parent class

    # posts could only be updated by their author OR by admin
    def test_func(self):                                # a function checking whether the user passes the required test
        post = self.get_object()
        if self.request.user == post.author or self.request.user.is_superuser:
            return True
        return False


# DetailView for each post
# UserPassesTestMixin will not allow anyone, but the post author to delete the post
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'                                   # in case of successful post deletion, redirect to homepage

    # posts could only be updated by their author OR by admin
    def test_func(self):                                # a function checking whether the user passes the required test
        post = self.get_object()
        if self.request.user == post.author or self.request.user.is_superuser:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})  # the last variable is the context dictionary to be passed to the about template
