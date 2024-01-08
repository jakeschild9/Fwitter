from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) # unique key for user
    id_user = models.IntegerField() # users id
    bio = models.TextField(blank=True) # allows bio to be blank
    profileimg = models.ImageField(upload_to='profile_images', default='wink.png') # uploading pfp to media folder, and having defalut pfp
    location = models.CharField(max_length=100, blank=True) # adds max length and allows no location from user

    def __str__(self): # shows username in admin panel instead of 'objects'
        return self.user.username
