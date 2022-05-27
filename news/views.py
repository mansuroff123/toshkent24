from django.shortcuts import render
from hitcount.views import HitCountDetailView
from django.views.generic import ListView
from .models import *
import requests
from django.db.models import Q


class PostListView(ListView):
    model = PostModel
    template_name = 'main/index.html'
    context_object_name = 'posts'
    # set to True to count the hit
    count_hit = True

    def get_queryset(self):
        qs = PostModel.objects.all()
        q = self.request.GET.get('q')
        if q:
            qs = qs.filter(Q(title__icontains=q) | Q(description__icontains=q))
            return qs
        qs = PostModel.objects.order_by('-pk')

        category = self.request.GET.get('cat')
        if category:
            return qs.filter(category_id=category)
        return qs

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)

        r = requests.get('https://nbu.uz/en/exchange-rates/json/', '')
        data = r.json()
        currency = []
        for i in data:
            if i['code'] == 'USD':
                currency.append(('&#36;', i['cb_price']))
            elif i['code'] == 'RUB':
                currency.append(('&#8381;', i['cb_price']))
            elif i['code'] == 'EUR':
                currency.append(('&#8364;', i['cb_price']))

        context['currency'] = currency
        context['last_posts'] = PostModel.objects.all().order_by('-pk')[:6]
        context['category'] = CategoryModel.objects.all()
        context.update({
            'popular_posts': PostModel.objects.order_by('-hit_count_generic__hits')[:4],
        })
        return context


class PostDetailView(HitCountDetailView):
    model = PostModel
    template_name = 'main/post_detail.html'
    context_object_name = 'post'
    slug_field = 'slug'
    # set to True to count the hit
    count_hit = True

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['category'] = CategoryModel.objects.all()
        context.update({
            'popular_posts': PostModel.objects.order_by('-hit_count_generic__hits')[:4],
        })
        return context


