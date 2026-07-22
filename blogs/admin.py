from django.contrib import admin
from .models import Category, Blogs, Comments

# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('id', 'title', 'category', 'author', 'status', 'is_featured')
    search_fields = ('id', 'title', 'category__category_name', 'status')
    list_editable = ('is_featured',)


admin.site.register(Comments)
admin.site.register(Category)
admin.site.register(Blogs, BlogAdmin)





