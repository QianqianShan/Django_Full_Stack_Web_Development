from django.db import models
from imagekit.models import ProcessedImageField
from django.urls import reverse

# create customzied user model
from django.contrib.auth.models import AbstractUser

# Create your models here.
class FunAppUser(AbstractUser):
    # customized profile picture
    profile_pic = ProcessedImageField(
                upload_to = 'static/images/profiles',
                format = 'JPEG',
                options = {'quality':200},
                blank = True,
                null = True,
                )
    def get_followings(self):
        # obtain all connections, and keep only those has creators of self
        connections = UserConnection.objects.filter(creator == self)

    def get_followers(self):
        # obtain all connections, and keep only those follow self
        connections = UserConnection.objects.filter(following == self)
    # tell if self is followed by user
    def is_followed_by(self, user):
        followers = UserConnection.objects.filter(following == self)
        return followers.filter(creator == user).exists()
    def __str__(self):
        return self.username



class UserConnection(models.Model):
    creator = models.ForeignKey(
    FunAppUser,
    on_delete = models.CASCADE,
    related_name = 'creators'
    )

    following = models.ForeignKey(
    FunAppUser,
    on_delete = models.CASCADE,
    related_name = 'followings'
    )

    def __str__(self):
        return self.creator.username + 'Follows' + self.following.username
# create a post class inherited from models.Model
# Post includes two fields: title and image
class Post(models.Model):
    author = models.ForeignKey(
             FunAppUser,
             on_delete = models.CASCADE,
             related_name = 'posts',
             blank = True,
             null = True,)
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
    # count how many likes
    def get_like_count(self):
        return self.likes.count()
    # count how many comments
    def get_comment_count(self):
        return self.comments.count()



class Comment(models.Model):
    # foreignkey of database linked to Post
    # related_name = 'comments' so that post.comments
     # can show all comments of current Post
    post = models.ForeignKey(to = Post,
           on_delete = models.CASCADE,
           related_name = 'comments')
    # who wrote the comments
    user = models.ForeignKey(
           FunAppUser,
           on_delete = models.CASCADE,
           related_name = 'comments'
    )

    comment = models.CharField(max_length = 140)
    posted_on = models.DateTimeField(
                auto_now_add = True,
                editable = False)

    def __str__(self):
        return self.comment

class Like(models.Model):
    post = models.ForeignKey(Post,
           on_delete = models.CASCADE,
           related_name = 'likes',)
    user = models.ForeignKey(FunAppUser,
           on_delete = models.CASCADE)

    # class Meta:
    #     unique_together = ("post", "user")

    def __str__(self):
        return 'Like: ' + self.user.username + ' ' + self.post.title
