from django.contrib import admin
from app.models import User,UserConfirmation, Post, Media, Comment

admin.site.register([User,UserConfirmation, Post, Media, Comment])
