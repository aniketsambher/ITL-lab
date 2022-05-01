from django.contrib import admin
import site
from webapp.models import BlogPost
# Register your models here.
from webapp import models

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'timestamp')
admin.site.register(models.BlogPost,BlogPostAdmin)
