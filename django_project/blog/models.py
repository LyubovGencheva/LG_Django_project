from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse                                 # 'reverse' function will return the full url to a route as a string


class Post(models.Model):
    title = models.CharField(max_length=300)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)    # if no specific date was added, it sets that to today
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # if a user is deleted, then all their posts would be deleted
                                                                # ForeignKey relation means that an Author(User) can have many posts, but a post can only have one Author

    def __str__(self):
        return self.title

    # returns the path to a specific post instance
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})   # will return as a string the full path to the post with that pk detail page