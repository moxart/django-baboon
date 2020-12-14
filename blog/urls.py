from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.HomeView.as_view(), name='homepage'),

    path('post/<slug:slug>', views.PostSingleView.as_view(), name='post-single'),

    path('post/category/<slug:slug>/', views.PostCategoryView.as_view(), name='post-category'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
