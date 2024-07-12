from django.urls import path
from . import views

app_name = 'myblog'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:blog_id>/', views.single_blog, name='blog_id'),
    path('add/', views.add_blog, name='add_blog')
]