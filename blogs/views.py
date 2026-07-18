from  django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect, get_object_or_404

from .forms import RegistrationForm
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


def blogs(request, slug):
    single_post = get_object_or_404(Blogs, slug=slug, status='Published')
    return render(request, 'blog_main/blogs.html', {'single_post':single_post})



from django.db.models import Q

from django.shortcuts import render
from django.db.models import Q
from .models import Blogs

def search(request):
    keyword = request.GET.get("keyword", "").strip()

    blogs = Blogs.objects.filter(status="Published")

    if keyword:
        blogs = blogs.filter(
            Q(title__icontains=keyword) |
            Q(short_description__icontains=keyword) |
            Q(blog_body__icontains=keyword)
        ).distinct()

    context = {
        "blogs": blogs,
        "keyword": keyword,
    }

    return render(request, "blog_main/search.html", context)


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register')
    else:
        form = RegistrationForm()
    context = {
        'form': form,
    }
    return render(request, 'blog_main/register.html', context)


from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm







def login_view(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == 'POST' and form.is_valid():
        auth.login(request, form.get_user())
        return redirect('home')

    return render(request, 'blog_main/login.html', {'form': form})

def logout(request):
    auth.logout(request)
    return redirect('home')