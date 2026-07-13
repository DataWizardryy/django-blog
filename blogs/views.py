from django.shortcuts import render, redirect, get_object_or_404
from .models import Blogs, Category


# Create your views here.

def category_view(request, category_id):
    posts = Blogs.objects.filter(status='Published', category=category_id)
    category = get_object_or_404(Category, pk=category_id)

    context = {
        'posts': posts,
        'category': category
    }
    return render(request, 'blog_main/post_by_category.html', context)
