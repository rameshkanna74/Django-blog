from django.urls import path
from . import views

app_name = 'blog'  # Important for namespaced URLs

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/create/', views.post_create, name='post_create'),
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),
    path('post/<slug:slug>/edit/', views.post_edit, name='post_edit'),
    path('post/<slug:slug>/delete/', views.post_delete, name='post_delete'),
    path('category/<slug:slug>/', views.post_list_by_category, name='post_list_by_category'),
    path('tag/<slug:slug>/', views.post_list_by_tag, name='post_list_by_tag'),
    path('post/<slug:slug>/publish/', views.post_publish, name='post_publish'),
    path('post/<slug:slug>/unpublish/', views.post_unpublish, name='post_unpublish'),
]
