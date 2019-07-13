from django.db import models
from imagekit.models import ProcessedImageField

# Create your models here.
# create a post class inherited from models.Model
# Post includes two fields: title and image
class Post(models.Model):
    # https://docs.djangoproject.com/en/2.2/ref/models/fields/
    # can be blank / null
    title = models.TextField(blank = True, null = True)
    image = ProcessedImageField(
    upload_to = 'static/images/posts',
    format = 'JPEG',
    options = {'quality':100},
    blank = True,
    null = True,
    )

    def __str__(self):
        return self.title
