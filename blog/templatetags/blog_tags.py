from django import template
from blog.models import Post , category
register = template.Library()


@register.simple_tag(name = 'totalposts')
def function():
    posts = Post.objects.filter(status = 1).count()
    return posts


@register.filter
def snippet(a):
    return a[:100]


@register.inclusion_tag('blog/popularposts.html')
def latestposts(arg=3):
    posts = Post.objects.filter(status=1).order_by("-published_date")[:arg]
    return{'posts':posts}


@register.inclusion_tag('blog/blog-categories.html')
def postcategories():
    posts = Post.objects.filter(status=1)
    categories = category.objects.all()
    cat_dict = {}
    for name in categories:
        cat_dict [name] = posts.filter(category=name).count()
    return{'categories':cat_dict}