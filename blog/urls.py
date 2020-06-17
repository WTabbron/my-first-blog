
from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<pk>/delete', views.post_delete, name='post_delete'),
    path('drafts/', views.post_draft_list, name='post_draft_list'),
    path('post/<pk>/post', views.post, name='post'),
]
