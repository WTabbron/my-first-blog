
from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('draft/<int:pk>/edit/', views.draft_edit, name='draft_edit'),
    path('draft/<int:pk>/', views.draft_detail, name='draft_detail'),
    path('post/<pk>/delete', views.post_delete, name='post_delete'),
    path('drafts/', views.post_draft_list, name='post_draft_list'),
    path('post/<pk>/post', views.post, name='post'),
    path('post/new/publish', views.post_new_publish, name='post_new_publish'),
    path('post/new/draft', views.post_new_draft, name='post_new_draft'),
]
