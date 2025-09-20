from django.urls import path
from blog.views import *

app_name = "blog"

urlpatterns = [
    path('',blog_view,name = 'blog-home'),
    path('<int:pid>',blog_single,name = 'blog-single'),
    path('author/<str:author_username>' , blog_view,name = 'author'),
    path('category/<str:cat_name>',blog_category,name = 'category'),
    path('search/' , blog_search , name = 'search'),



]

