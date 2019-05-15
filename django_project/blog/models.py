from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=300)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)    # if no specific date was added, it sets that to today
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # if a user is deleted, then all their posts would be deleted
                                                                # ForeignKey relation means that an Author(User) can have many posts, but a post can only have one Author

    def __str__(self):
        return self.title