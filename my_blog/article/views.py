from django.shortcuts import render
from django.http import HttpResponse
from article.models import Arcicle
from datetime import datetime
from django.http import Http404


# Create your views here.
def home(request):
    post_list = Arcicle.objects.all()
    return render(request,'home.html',{'post_list':post_list})

def detali(request,id):
    try:
        post = Arcicle.objects.get(id=str(id))
    except Arcicle.DoesNotExist:
        raise Http404
    return render(request,'post.html',{'post' : post})

def archives(request):
    try:
        post_list = Arcicle.objects.all()
    except Arcicle.DoesNotExist:
        raise Http404
    return render(request,'archives.html',{'post_list' : post_list,
                                     'error':False})
def searchTag(request,tag):
    try:
        post_list = Arcicle.objects.filter(category=tag)
    except Arcicle.DoesNotExist:
        raise Http404
    return render(request,'tag.html',{'post_list':post_list})