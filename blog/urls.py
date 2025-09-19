from django.urls import path
from blog.views import *

urlpatterns = [
    path('blog-home',blog_view,name = 'blog-home'),
    path('<int:pid>',blog_single,name = 'blog-single'),


]

