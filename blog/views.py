from django.views import generic

from .forms.NewPostForm import NewPostForm
from .forms.UpdatePostForm import UpdatePostForm
from .models import *


# BLOG

class PostList(generic.ListView):
    queryset = Post.objects.filter(status="publish").order_by('-published_at')
    template_name = 'blog/index.html'


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'blog/layouts/post_update.html'


# DASHBOARD

class DashboardList(generic.ListView):
    queryset = Post.objects.filter(status="publish").order_by('-published_at')
    template_name = 'dashboard/index.html'


class PostCreateView(generic.FormView):
    template_name = 'dashboard/layouts/post_new.html'
    form_class = NewPostForm
    success_url = '/dashboard/post/create'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class PostUpdateView(generic.UpdateView):
    template_name = 'dashboard/layouts/post_update.html'
    model = Post
    form_class = UpdatePostForm

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)