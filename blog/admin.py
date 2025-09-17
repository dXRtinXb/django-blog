from django.contrib import admin
from blog.models import Post

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name' , 'email' , 'created_date']
admin.site.register(Post)
