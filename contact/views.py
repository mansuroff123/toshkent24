from django.shortcuts import render, reverse
from django.views.generic import CreateView
from .forms import ContactModelForm
from news.models import CategoryModel


class ContactView(CreateView):
    form_class = ContactModelForm
    template_name = 'main/contact.html'\


    def get_context_data(self, **kwargs):
        context = super(ContactView, self).get_context_data(**kwargs)
        context['category'] = CategoryModel.objects.all()
        return context

    def get_success_url(self):
        return reverse('contacts:contact')

