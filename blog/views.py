from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from blog.models import Blog
from blog.models import Trails
from blog.models import MyTunes


def all_blogs(request):
    ## blogsMyTunes = Blog.objects.count()
    ##or I can specify some sorting of the records
    blogs = Blog.objects.order_by('-date')[:10]
    return render(request, 'all_blogs.html', {'blogs':blogs})

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    ##return render(request, 'detail.html', {'id':blog_id})
    return render(request, 'detail.html', {'blog':blog})
def trails(request):
    trails = Trails.objects.all()
    return render(request, 'trails.html', {'trails':trails})

def mytunes(request):
    mytunes = MyTunes.objects.all()
    return render(request, 'mytunes.html', {'mytunes':mytunes})
