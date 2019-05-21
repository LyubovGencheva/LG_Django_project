from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # if the User is deleted, the Profile will be deleted too, but not vice-versa
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    about = models.CharField(max_length=350, null=True, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    # Override the save method to resize the profile pic before saving it.
    def save(self, *args, **kwargs):                # *args, **kwargs have to be present when we override
        super().save(*args, **kwargs)               # running the save method on the parent class
                                                    # will save the uploaded image just as it is
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:     # resizes if neccessary
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)               # saves the resized image to the original path