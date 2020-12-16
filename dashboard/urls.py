from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required

from . import views

app_name = 'dashboard'
urlpatterns = [
    path('dashboard/', views.DashboardListView.as_view(), name='dashboard'),
    path('dashboard/posts', views.PostListView.as_view(), name='posts'),
    path('dashboard/post/create', views.PostCreateView.as_view(), name='post-create'),
    path('dashboard/post/<int:pk>/edit', views.PostUpdateView.as_view(), name='post-edit'),
    path('dashboard/categories', views.CategoryListView.as_view(), name='categories'),
    path('dashboard/category/create', views.CategoryCreateView.as_view(), name='category-create'),
    path('dashboard/category/<int:pk>/edit', views.CategoryUpdateView.as_view(), name='category-edit'),
    path('dashboard/users', views.UserListView.as_view(), name='users'),
    path('dashboard/user/create', views.UserCreateView.as_view(), name='user-create'),
    path('dashboard/user/<int:pk>/edit', views.UserUpdateView.as_view(), name='user-edit'),
    path('dashboard/media/upload', views.MediaUploadNewView.as_view(), name='media-upload'),
    path('dashboard/media/uploaded', views.MediaUploadListView.as_view(), name='media-upload-list'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
