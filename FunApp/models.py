from django.db import models
from imagekit.models import ProcessedImageField
from django.urls import reverse

# create customzied user model
from django.contrib.auth.models import AbstractUser

# Create your models here.
# create a post class inherited from models.Model
# Post includes two fields: title and image
class Post(models.Model):
    # https://docs.djangoproject.com/en/2.2/ref/models/fields/
    # title and image can be blank / null
    title = models.TextField(blank = True, null = True)
    image = ProcessedImageField(
    upload_to = 'static/images/posts',
    format = 'JPEG',
    options = {'quality':200},
    blank = True,
    null = True,
    )

    def __str__(self):
        # when str() is called for Post object, return its title
        return self.title

    def get_absolute_url(self):
        # self.id: primary key of the currently created model
        # reverse url from its name
        return reverse('post_detail', args = [str(self.id)])

class FunAppUser(AbstractUser):
    # customized profile picture
    profile_pic = ProcessedImageField(
                upload_to = 'static/images/profiles',
                format = 'JPEG',
                options = {'quality':200},
                blank = True,
                null = True,
                )
