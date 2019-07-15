from django.contrib import admin
from FunApp.models import Post, FunAppUser, Comment, Like, UserConnection

# Register your models here.
admin.site.register(Post)
admin.site.register(FunAppUser)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(UserConnection)
