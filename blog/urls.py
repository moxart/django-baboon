from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from . import views

app_name = 'blog'
urlpatterns = [
    # blog
    path('', views.PostList.as_view(), name='homepage'),
    path('post/<slug:slug>/', views.PostDetail.as_view(), name='post-detail'),
    # dashboard
    path('dashboard/', views.DashboardList.as_view(), name='dashboard'),
    path('dashboard/posts', views.PostListView.as_view(), name='dsh-posts'),
    path('dashboard/post/create', views.PostCreateView.as_view(), name='dsh-post-create'),
    path('dashboard/post/<int:pk>/edit', views.PostUpdateView.as_view(), name='dsh-post-edit'),
    # category
    path('dashboard/categories', views.CategoryListView.as_view(), name='dsh-categories'),
    path('dashboard/category/create', views.CategoryCreateView.as_view(), name='dsh-category-create'),
    # user
    path('dashboard/users', views.UserListView.as_view(), name='dsh-users'),
    path('dashboard/user/create', views.UserCreateView.as_view(), name='dsh-user-create'),
    path('dashboard/user/<int:pk>/edit', views.UserUpdateView.as_view(), name='dsh-user-edit'),
    # auth
    path('login/', views.LoginView.as_view(), name='login'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
