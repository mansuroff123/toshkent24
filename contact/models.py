from django.db import models
from django.utils.translation import gettext_lazy as _


class ContactModel(models.Model):
    name = models.CharField(max_length=64, verbose_name=_('name'))
    email = models.EmailField(verbose_name=_('email'))
    number = models.CharField(max_length=13, verbose_name=_('number'))
    title = models.CharField(max_length=100, verbose_name=_('title'))
    text = models.TextField(verbose_name=_('text'))
    file = models.FileField(null=True)
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('created at')
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'contact'
        verbose_name_plural = 'contacts'

