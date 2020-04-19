from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.utils import timezone
from django.urls import reverse
from django.db import models
from django.conf import settings
from django.utils.text import slugify


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pic')
    my_story = models.CharField(max_length=200, null=True)

    def __str__(self):
        return f'{self.user.username} Profile'


class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='images_created',
                             on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/%Y/%m/%d/')
    caption = models.TextField(db_index=True)
    created = models.DateTimeField(default=timezone.now)
    user_like = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                       related_name='images_liked',
                                       blank=True)

    def __str__(self):
        return self.caption

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

