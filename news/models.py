from django.db import models
from django.utils.translation import gettext_lazy as _
from ckeditor_uploader.fields import RichTextUploadingField


class CategoryModel(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('category'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')


class PostViewModel(models.Model):
    post_views = models.IntegerField(default=0)

    def __str__(self):
        return self.post_views

    class Meta:
        verbose_name = _('view')
        verbose_name_plural = _('views')


class PostModel(models.Model):
    title = models.CharField(max_length=255, verbose_name=_('title'))
    description = RichTextUploadingField(verbose_name=_('description'))
    img = models.ImageField(upload_to='posts/')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name=_('create at'))
    modified = models.DateTimeField(auto_now=True, verbose_name=_('modified'))
    views = models.ManyToManyField(PostViewModel, related_name='post_views', blank=True)
    category = models.ForeignKey(
        on_delete=models.PROTECT,
        related_name='post_category',
        verbose_name=_('category')
    )

    class Meta:
        verbose_name = _('post')
        verbose_name_plural = _('posts')

    def __str__(self):
        return self.title
