from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from.models import Polls

# Create your views here.
class PostView():
    # model = x (add a html model file with css shit)
    template_name = ''

class CreatePostView():
    #same as above
    template_name = ''

class CommentView():
    #^^
    template_name = ''
