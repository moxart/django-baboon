from django.views import generic

from .models import Post, Category


class PostList(generic.ListView):
    queryset = Post.objects.filter(status="publish").order_by('-published_at')
    template_name = 'blog/index.html'


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'blog/layouts/post_detail.html'
