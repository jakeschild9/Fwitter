import uuid
from datetime import datetime
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # unique key for user
    id_user = models.IntegerField()  # users id
    bio = models.TextField(blank=True)  # allows bio to be blank
    profileimg = models.ImageField(upload_to='profile_images',
                                   default='wink.png')  # uploading pfp to media folder, and having defalut pfp
    location = models.CharField(max_length=100, blank=True)  # adds max length and allows no location from user

    def __str__(self):  # shows username in admin panel instead of 'objects'
        return self.user.username


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.CharField(max_length=100)
    image = models.ImageField(upload_to='post_images')
    caption = models.TextField()
    created_at = models.DateTimeField(default=datetime.now)
    no_of_likes = models.IntegerField(default=0)

    def __str__(self):
        return self.user


class LikePost(models.Model):
    post_id = models.CharField(max_length=500)
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.username


class FollowersCount(models.Model):
    follower = models.CharField(max_length=100)  # follower
    user = models.CharField(max_length=100)  # person being followed

    def __str__(self):
        return self.user