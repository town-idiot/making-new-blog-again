from django.contrib import admin

# Register your models here.
from .models import Post

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ['Slug','Published', 'Update']

admin.site.register(Post,PostAdmin)