from django.urls import path, include
from .views import PostListView, PostDetailView


app_name = 'news'

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    # path('<int:pk>/post/', PostDetailView.as_view(), name='post_detail'),
    path('<slug:slug>/', PostDetailView.as_view(), name='detail'),
    path('hitcount/', include(('hitcount.urls', 'hitcount'), namespace='hitcount')),
]