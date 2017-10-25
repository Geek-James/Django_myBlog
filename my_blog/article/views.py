from django.shortcuts import render
from django.http import HttpResponse
from article.models import Arcicle
from datetime import datetime


# Create your views here.
def home(request,):
    post_list = Arcicle.objects.all()
    return render(request,'home.html',{'post_list':post_list})

def detali(request,my_args):

    post = Arcicle.objects.all()[int(my_args)]
    str = ("title = %s, category = %s, date_time = %s, content = %s, author = %s"
           % (post.title, post.category, post.date_time, post.content,post.author))
    return HttpResponse(str)

def test(request):
    return render(request,'test.html',{'current_time':datetime.now()})