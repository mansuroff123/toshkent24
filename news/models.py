from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.template.defaultfilters import slugify
from django.utils.translation import gettext_lazy as _
from ckeditor_uploader.fields import RichTextUploadingField
from hitcount.models import HitCount
from django.urls import reverse


class CategoryModel(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('category'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')


class PostModel(models.Model):
    title = models.CharField(max_length=255, verbose_name=_('title'))
    description = RichTextUploadingField(verbose_name=_('description'))
    img = models.ImageField(upload_to='posts/')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name=_('create at'))
    modified = models.DateTimeField(auto_now=True, verbose_name=_('modified'))
    slug = models.SlugField(unique=True, max_length=100)
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk',
                                        related_query_name='hit_count_generic_relation')
    category = models.ForeignKey(
        CategoryModel,
        on_delete=models.PROTECT,
        related_name='post_relate',
        verbose_name=_('category')
    )

    class Meta:
        verbose_name = _('post')
        verbose_name_plural = _('posts')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news:detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super(PostModel, self).save(*args, **kwargs)




