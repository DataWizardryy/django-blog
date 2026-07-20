from django.urls import path
from . import views

urlpatterns =[
    path('', views.dashboard_view, name='dashboard'),
    path('categories/', views.categories_view, name='categories'),
    path('categories/add/', views.add_category_view, name='add_category'),
    path('categories/edit/<int:pk>/', views.edit_category_view, name='edit_category'),
    path('categories/delete/<int:pk>/', views.delete_category_view, name='delete_category'),

    path('posts/', views.posts_view, name='posts'),
    path('posts/add/', views.add_post_view, name='add_post'),
    path('posts/edit/<int:pk>', views.edit_post_view, name='edit_post'),
    path('posts/delete/<int:pk>', views.delete_post_view, name='delete_post'),

    path('users/', views.users_view, name='users'),
    path('users/add/', views.add_user_view, name='add_user'),
    path('users/edit/<int:pk>/', views.edit_user_view, name='edit_user'),
    path('users/delete/<int:pk>/', views.delete_user_view, name='delete_user'),


]