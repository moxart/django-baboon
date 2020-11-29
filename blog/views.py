from django.views import generic
from django.contrib.auth import login
from django.http import HttpResponseRedirect

from .forms.UserLoginForm import UserLoginForm
from .forms.UserCreateForm import UserCreateForm
from .forms.UserUpdateForm import UserUpdateForm
from .forms.PostCreateForm import PostCreateForm
from .forms.PostUpdateForm import PostUpdateForm
from .forms.CategoryCreateForm import CategoryCreateForm

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


class PostListView(generic.ListView):
    model = Post
    template_name = 'dashboard/layouts/posts.html'
    paginate_by = 10


class PostCreateView(generic.FormView):
    template_name = 'dashboard/layouts/post_new.html'
    form_class = PostCreateForm
    success_url = '/dashboard/post/create'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class PostUpdateView(generic.UpdateView):
    template_name = 'dashboard/layouts/post_update.html'
    model = Post
    form_class = PostUpdateForm

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class CategoryListView(generic.ListView):
    model = Category
    template_name = 'dashboard/layouts/categories.html'


class CategoryCreateView(generic.CreateView):
    template_name = 'dashboard/layouts/category_new.html'
    form_class = CategoryCreateForm
    success_url = '/dashboard/categories'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class UserListView(generic.ListView):
    template_name = 'dashboard/layouts/users.html'
    model = User


class UserUpdateView(generic.UpdateView):
    template_name = 'dashboard/layouts/user_edit.html'
    model = User
    form_class = UserUpdateForm
    success_url = '/dashboard/users'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class UserCreateView(generic.FormView):
    template_name = 'dashboard/layouts/user_new.html'
    form_class = UserCreateForm
    success_url = '/dashboard/user/create'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class LoginView(generic.FormView):
    template_name = 'dashboard/layouts/login.html'
    form_class = UserLoginForm

    def form_valid(self, form):
        login(self.request, form.get_user())
        return HttpResponseRedirect('/dashboard')
