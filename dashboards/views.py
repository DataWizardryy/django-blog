from django.shortcuts import render, redirect, get_object_or_404
from blogs.models import Category, Blogs
from django.contrib.auth.decorators import login_required

from .forms import CategoryForm


# Create your views here.
@login_required(login_url='login')
def dashboard_view(request):
    category_count = Category.objects.all().count()
    blogs_count = Blogs.objects.all().count()

    context ={
        'category_count': category_count,
        'blogs_count': blogs_count
    }
    return render(request, 'dashboard/dashboard.html', context)


def categories_view(request):
    return render(request, 'blog_main/categories.html')


def add_category_view(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories')
    form = CategoryForm()
    context = {
        'form': form,
    }
    return render(request, 'dashboard/add_category.html', context)


def edit_category_view(request, pk):
    category = get_object_or_404(Category, pk=pk)
    form = CategoryForm(instance=category)
    if request.method == 'POST':
        form = CategoryForm(request.POST,instance=category)
        if form.is_valid():
            form.save()
            return redirect('categories')

    context = {
        'form': form,
        'category': category,
    }
    return render(request, 'dashboard/edit_category.html', context)


def delete_category_view(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('categories')

    context ={
        'category': category,

    }

    return render(request, 'dashboard/delete_category.html', context)
