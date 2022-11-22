from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html


from typeidea.custom_site import custom_site
from typeidea.base_admin import BaseOwnerAdmin
from .models import Category, Tag, Post
from .adminforms import PostAdminForm

# Register your models here.


class PostInline(admin.TabularInline):
    fields = ('title', 'decs')
    extra = 1
    model = Post

@admin.register(Category, site=custom_site)
class CategoryAdmin(BaseOwnerAdmin):
    list_display = ('name', 'status', 'is_nav', 'created_time')
    fields = ('name', 'status', 'is_nav')
    inlines = [PostInline, ]

    def post_count(self, obj):
        return obj.post_set.count()
    post_count.short_description = '文章数量'


@admin.register(Tag, site=custom_site)
class TagAdmin(BaseOwnerAdmin):
    list_display = ('name', 'status', 'created_time')
    fields = ('name', 'status')

    


class CategoryOwnerFilter(admin.SimpleListFilter):
    """自定义过滤器只展示当前用户分类"""

    title = '分类过滤器'
    parameter_name = 'owner_category'

    def lookups(self, request, model_admin):
        return Category.objects.filter(owner=request.user).values_list('id', 'name')

    def queryset(self, request, queryset):
        category_id = self.value()
        if category_id:
            return queryset.filter(category_id=self.value())
        return queryset

@admin.register(Post, site=custom_site)
class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    list_display = ['title', 'category', 'status', 'created_time', 'owner', 'operator']
    list_display_link = []
    
    list_filter = [CategoryOwnerFilter]
    search_fields = ['title', 'category__name']

    actions_on_bottom = True
    actions_on_top = True

    save_on_top = True

    fieldsets = (
        ('基础配置', {
            'description': '基础配置描述',
            'fields': (
                ('title', 'category'),
                'status',
            ),
        }),
        ('内容',{
            'fields': (
                'decs',
                'content',
            ),
        }),
        ('额外信息', {
            'classes':('wide', ),
            'fields': ('tag', )
        })
    )
    filter_vertical = ('tag', )

    def operator(self, obj):
        return format_html(
            '<a href="{}">编辑</a>',
            reverse('cus_admin:blog_post_change', args=(obj.id,))
        )
    operator.short_description = '操作'

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(PostAdmin, self).save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super(PostAdmin, self).get_queryset(request)
        return qs.filter(owner=request.user)

