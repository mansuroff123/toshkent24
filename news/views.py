from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import PostModel


# Create your views here.


class PostListView(ListView):
    model = PostModel
    template_name = 'main/index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        qs = PostModel.objects.order_by('-pk')
        category = self.request.GET.get('category')
        if category:
            return qs.filter(categories__title=category)
        return qs

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data()
        context['last_posts'] = PostModel.objects.all().order_by('-pk')[:6]
        context['last_view'] = PostModel.objects.all().order_by('-views')[:4]

    @staticmethod
    def post_view(post_id):
        blog_object = PostModel.objects.get(id=post_id)
        blog_object.blog_views = blog_object.blog_views + 1
        blog_object.save()


class PostDetailView(DetailView):
    model = PostModel
    template_name = 'main/'
    context_object_name = 'post'

