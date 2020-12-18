from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import reverse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic
from django.views.generic import RedirectView
from django.views.generic import TemplateView

from dashboard.models import Post, Category, Tag, Media

from .forms.CategoryCreateForm import CategoryCreateForm
from .forms.CategoryUpdateForm import CategoryUpdateForm
from .forms.TagCreateForm import TagCreateForm
from .forms.TagUpdateForm import TagUpdateForm
from .forms.MediaUploadForm import MediaUploadNewForm
from .forms.PostCreateForm import PostCreateForm
from .forms.PostUpdateForm import PostUpdateForm
from .forms.UserCreateForm import UserCreateForm
from .forms.UserLoginForm import UserLoginForm
from .forms.UserUpdateForm import UserUpdateForm


@method_decorator(login_required, name='dispatch')
class DashboardListView(TemplateView):
    queryset = Post.objects.filter(status="publish").order_by('-published_at')
    template_name = 'dashboard/index.html'


@method_decorator(login_required, name='dispatch')
class PostListView(generic.ListView):
    model = Post
    template_name = 'dashboard/layouts/posts.html'
    paginate_by = 10


@method_decorator(login_required, name='dispatch')
class PostCreateView(generic.CreateView):
    template_name = 'dashboard/layouts/post_new.html'
    form_class = PostCreateForm
    success_url = '/dashboard/posts'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class PostUpdateView(generic.UpdateView):
    template_name = 'dashboard/layouts/post_update.html'
    form_class = PostUpdateForm
    model = Post

    def form_valid(self, form):
        form.save(commit=True)
        return super(PostUpdateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('dashboard:post-edit', kwargs={'pk': self.object.pk})


@method_decorator(login_required, name='dispatch')
class PostDeleteView(generic.DeleteView):
    model = Post
    template_name = 'dashboard/layouts/post_confirm_delete.html'
    success_url = reverse_lazy('dashboard:posts')


@method_decorator(login_required, name='dispatch')
class CategoryListView(generic.ListView):
    model = Category
    template_name = 'dashboard/layouts/categories.html'


@method_decorator(login_required, name='dispatch')
class CategoryUpdateView(generic.UpdateView):
    template_name = 'dashboard/layouts/category_edit.html'
    model = Category
    form_class = CategoryUpdateForm
    success_url = '/dashboard/categories'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class CategoryCreateView(generic.CreateView):
    template_name = 'dashboard/layouts/category_new.html'
    form_class = CategoryCreateForm
    success_url = '/dashboard/categories'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class TagListView(generic.ListView):
    model = Tag
    template_name = 'dashboard/layouts/tags.html'


@method_decorator(login_required, name='dispatch')
class TagCreateView(generic.CreateView):
    template_name = 'dashboard/layouts/tag_new.html'
    form_class = TagCreateForm
    success_url = '/dashboard/tags'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class TagUpdateView(generic.UpdateView):
    template_name = 'dashboard/layouts/tag_edit.html'
    model = Tag
    form_class = TagUpdateForm
    success_url = '/dashboard/tags'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class UserListView(generic.ListView):
    model = User
    template_name = 'dashboard/layouts/users.html'


@method_decorator(login_required, name='dispatch')
class UserUpdateView(generic.UpdateView):
    template_name = 'dashboard/layouts/user_edit.html'
    model = User
    form_class = UserUpdateForm
    success_url = '/dashboard/users'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class UserCreateView(generic.FormView):
    template_name = 'dashboard/layouts/user_new.html'
    form_class = UserCreateForm
    success_url = '/dashboard/user/create'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class MediaUploadNewView(generic.FormView):
    template_name = 'dashboard/layouts/media_upload_new.html'
    form_class = MediaUploadNewForm
    success_url = '/dashboard/media/uploaded'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class MediaUploadListView(generic.ListView):
    model = Media
    template_name = 'dashboard/layouts/media_upload_list.html'
    paginate_by = 5


@method_decorator(login_required, name='dispatch')
class MediaDeleteView(generic.DeleteView):
    model = Media
    template_name = 'dashboard/layouts/media_confirm_delete.html'
    success_url = reverse_lazy('dashboard:media-upload-list')


class LoginView(generic.FormView):
    template_name = 'dashboard/layouts/login.html'
    form_class = UserLoginForm

    def form_valid(self, form):
        login(self.request, form.get_user())
        return HttpResponseRedirect('/dashboard')


class LogoutView(RedirectView):
    url = '/login/'

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)
