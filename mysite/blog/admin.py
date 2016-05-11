from django.contrib import admin
from .models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['date','title','img_path', 'draft']
    list_filter = ['date']
    list_editable = ['draft']
    search_fields = ['name']

    class Meta:
        model = Post

admin.site.register(Post, PostAdmin)
