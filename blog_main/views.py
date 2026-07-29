from django.shortcuts import render
from blogs.models import Category, Blogs
from sideBar.models import About


def home(request):
    featured_posts = Blogs.objects.filter(is_featured=True, status='Published').order_by('updated_at')
    posts = Blogs.objects.filter(is_featured=False, status='Published')

    try:
        about = About.objects.get()
    except:
        about = None

    context ={
        'featured_posts': featured_posts,
        'posts': posts,
        'about': about,
    }
    return render(request, 'blog_main/home.html', context)

