from django.views import generic

from dashboard.models import Post, Category


# BLOG
class HomeView(generic.ListView):
    model = Post
    template_name = 'blog/index.html'
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(status="publish").order_by('-published_at')
        context['categories'] = Category.objects.all()
        return context


class PostSingleView(generic.DetailView):
    model = Post
    template_name = 'blog/layouts/post/post-single.html'

    def get_context_data(self, **kwargs):
        context = super(PostSingleView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class PostCategoryView(generic.ListView):
    model = Category
    template_name = 'blog/layouts/post/post-category.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(
            category__slug=self.kwargs['slug']
        )
        context['categories'] = Category.objects.all()
        return context
