from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('post/<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
