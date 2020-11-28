from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from . import views

app_name = 'blog'
urlpatterns = [
    # blog
    path('', views.PostList.as_view(), name='home'),
    path('post/<slug:slug>/', views.PostDetail.as_view(), name='post-detail'),
    # dashboard
    path('dashboard/', views.DashboardList.as_view(), name='dashboard-home'),
    path('dashboard/post/create', views.PostCreateView.as_view(), name='post-create'),
    path('dashboard/post/<int:pk>/update', views.PostUpdateView.as_view(), name='post-update'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
