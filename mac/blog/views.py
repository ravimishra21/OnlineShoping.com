from django.shortcuts import render
from django.http import HttpResponse
from .models import Blogpost

# Create your views here.
def index(request):
    myposts = Blogpost.objects.all()
    print(myposts)
    # 'myposts':myposts ----->  for calling mypost ........
    # kisi ko call krne ke liye views.py ke return render me us object ko include krna padta h ....
    return render(request, 'blog/index.html',{'myposts':myposts})


def blogpost(request, id):
    post = Blogpost.objects.filter(post_id = id)[0]
    return render(request, 'blog/blogpost.html', {'post':post})

