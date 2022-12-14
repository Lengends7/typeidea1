from django.contrib.auth.models import User
from django.db import models

from django.template.loader import render_to_string

# Create your models here.

class Link(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = {
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '删除')
    }
    title = models.CharField(max_length=50, verbose_name='标题')
    href = models.URLField(max_length=200, verbose_name='链接')
    status = models.PositiveIntegerField(choices=STATUS_ITEMS, default=STATUS_NORMAL, verbose_name='状态')
    weight = models.PositiveIntegerField(default=1, choices=zip(range(1, 6),range(1, 6)), verbose_name='权重')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    owner = models.ForeignKey(User, verbose_name='作者')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = verbose_name_plural = '友链'

class SideBar(models.Model):
    STATUS_SHOW = 1
    STATUS_HIDE = 0
    STATUS_ITEMS = {
        (STATUS_SHOW, '展示'),
        (STATUS_HIDE, '隐藏'),
    }

    DISPLAY_HTML = 1
    DISPLAY_LATEST = 2
    DISPLAY_HOT = 3
    DISPLAY_COMMENT = 4
    SIDE_TYPE = {
        (DISPLAY_HTML, 'HTML'),
        (DISPLAY_LATEST, '最新文章'),
        (DISPLAY_HOT, '最热文章'),
        (DISPLAY_COMMENT, '最近评论')
    }

    title = models.CharField(max_length=50, verbose_name='名称')
    display_type = models.PositiveIntegerField(choices=SIDE_TYPE, default=1, verbose_name='展示类型')
    content = models.CharField(max_length=500, blank=True, verbose_name='内容', help_text='如果设置得内容不是html，可以为空')
    status = models.PositiveIntegerField(default=STATUS_SHOW, choices=STATUS_ITEMS, verbose_name='状态')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    owner = models.ForeignKey(User, verbose_name='作者')

    @classmethod
    def get_all(cls):
        return cls.objects.filter(status=cls.STATUS_SHOW)

    @property
    def content_html(self):
        from blog.models import Post
        from comment.models import Comment

        result = ''
        if self.display_type == self.DISPLAY_HTML:
            result = self.content
        elif self.display_type == self.DISPLAY_LATEST:
            context = {
                'posts': Post.latest_posts()
            }
            result = render_to_string('config/blocks/sidebar_posts.html',context),
        elif self.display_type == self.DISPLAY_HOT:
            context = {
                'posts':Post.hot_posts()
            }
            result = render_to_string('config/block/sidebar_posts.html',context)
        elif self.display_type == self.DISPLAY_COMMENT:
            context = {
                'comments': Comment.objects.filter(status=Comment.STATUS_NORMAL)
            }
            result = render_to_string('config/block/sidebar_comments.html',context)
        return result

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = verbose_name_plural = '侧边栏'
