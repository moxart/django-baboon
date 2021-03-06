from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

app_name = 'dashboard'
urlpatterns = [
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),

    path('dashboard/posts', views.PostListView.as_view(), name='posts'),
    path('dashboard/post/create', views.PostCreateView.as_view(), name='post-create'),
    path('dashboard/post/<int:pk>/edit', views.PostUpdateView.as_view(), name='post-edit'),
    path('dashboard/post/<int:pk>/delete', views.PostDeleteView.as_view(), name='post-delete'),

    path('dashboard/categories', views.CategoryListView.as_view(), name='categories'),
    path('dashboard/category/create', views.CategoryCreateView.as_view(), name='category-create'),
    path('dashboard/category/<int:pk>/edit', views.CategoryUpdateView.as_view(), name='category-edit'),

    path('dashboard/tag/create', views.TagCreateView.as_view(), name='tag-create'),
    path('dashboard/tags', views.TagListView.as_view(), name='tag-list'),
    path('dashboard/tag/<int:pk>/edit', views.TagUpdateView.as_view(), name='tag-edit'),

    path('dashboard/users', views.UserListView.as_view(), name='users'),
    path('dashboard/user/create', views.UserCreateView.as_view(), name='user-create'),
    path('dashboard/user/<int:pk>/edit', views.UserUpdateView.as_view(), name='user-edit'),

    path('dashboard/media/upload', views.MediaUploadNewView.as_view(), name='media-upload'),
    path('dashboard/media/uploaded', views.MediaUploadListView.as_view(), name='media-upload-list'),
    path('dashboard/media/delete/<int:pk>', views.MediaDeleteView.as_view(), name='media-delete'),

    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
