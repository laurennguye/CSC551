from django.contrib import admin
from .models import User, Post, Comment, Poll, PollOption, PollVote, Like

# Register your models here.

admin.site.register(User)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Poll)
admin.site.register(PollOption)
admin.site.register(PollVote)
admin.site.register(Like)