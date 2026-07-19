from django.urls import path
from . import views

urlpatterns =[
    path('', views.dashboard_view, name='dashboard'),
    path('categories/', views.categories_view, name='categories'),
    path('categories/add/', views.add_category_view, name='add_category'),
    path('categories/edit/<int:pk>/', views.edit_category_view, name='edit_category'),
    path('categories/delete/<int:pk>/', views.delete_category_view, name='delete_category'),
]