from django.contrib import admin


from .models import Comment

# Register your models here.

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('target', 'content', 'status', 'created_time')
    fields = ('target', 'content', 'nickname', 'status')

    