from django.contrib import admin
from blog.models import Post,Category, Legales, Sobremi

# Register your models here.

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Legales)
admin.site.register(Sobremi)